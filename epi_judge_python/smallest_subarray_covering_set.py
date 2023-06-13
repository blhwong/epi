import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    s, e = -float('inf'), float('inf')
    start = 0
    d = {}
    for end in range(len(paragraph)):
        word = paragraph[end]
        if word not in keywords:
            continue
        if word not in d:
            d[word] = 0
        d[word] += 1
        while len(d) == len(keywords):
            if end - start < e - s:
                e, s = end, start
            start_word = paragraph[start]
            start += 1
            if start_word not in d:
                continue
            d[start_word] -= 1
            if d[start_word] == 0:
                del d[start_word]

    return Subarray(s, e)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
