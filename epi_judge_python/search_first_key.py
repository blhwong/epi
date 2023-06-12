from typing import List

from test_framework import generic_test


def search_first_of_k(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1

    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            ans = mid
            right = mid - 1
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
