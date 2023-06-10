from heapq import *
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    ans = []
    min_heap, max_heap = [], []
    for val in sequence:
        heappush(max_heap, -heappushpop(min_heap, val))
        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))

        median = min_heap[0]
        if len(min_heap) == len(max_heap):
            median = (min_heap[0] - max_heap[0]) / 2

        ans.append(median)

    return ans


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
