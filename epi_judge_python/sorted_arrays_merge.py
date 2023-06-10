from heapq import *
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    ans = []
    min_heap = []
    for arr in sorted_arrays:
        heappush(min_heap, (arr[0], arr, 0))

    while min_heap:
        val, arr, i = heappop(min_heap)
        ans.append(val)
        if i + 1 < len(arr):
            heappush(min_heap, (arr[i + 1], arr, i + 1))

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
