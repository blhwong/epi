import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    intervals.sort(key=lambda x: (x.left.val, not x.left.is_closed))
    ans = []
    left, right = intervals[0]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        is_add_interval = (
            interval.left.val > right.val or
            all((interval.left.val == right.val, not interval.left.is_closed, not right.is_closed))
        )
        if is_add_interval:
            ans.append(Interval(left, right))
            left, right = interval
        else:
            if interval.right.val > right.val:
                right = interval.right
            elif interval.right.val == right.val and interval.right.is_closed:
                right = interval.right

    ans.append(Interval(left, right))
    return ans


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
