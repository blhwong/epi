from heapq import *
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    ans = []
    min_heap = []
    val = next(sequence, None)
    while val is not None:
        for _ in range(k):
            if val is not None:
                heappush(min_heap, val)
            val = next(sequence, None)
        while min_heap:
            ans.append(heappop(min_heap))
    return ans


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
