import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(a: List[Event]) -> int:
    arr = []
    for event in a:
        arr.append((event.start, True))
        arr.append((event.finish, False))
    arr.sort(key=lambda el: (el[0], not el[1]))

    ans, curr = 0, 0

    for _, is_start in arr:
        if is_start:
            curr += 1
            ans = max(ans, curr)
        else:
            curr -= 1

    return ans


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
