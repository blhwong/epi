from typing import List

from test_framework import generic_test


def search_smallest(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < arr[ans]:
            ans = mid

        if arr[mid] <= arr[right]:
            right = mid - 1
        else:
            left = mid + 1

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
