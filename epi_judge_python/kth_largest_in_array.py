from typing import List
from random import randint

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, arr: List[int]) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        p = partition(arr, left, right)

        if p == k - 1:
            return arr[p]

        if p < k - 1:
            left = p + 1
        else:
            right = p - 1


def partition(arr, left, right):
    rand_idx = randint(left, right)
    arr[right], arr[rand_idx] = arr[rand_idx], arr[right]
    p = arr[right]

    for i in range(left, right):
        if arr[i] > p:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[left], arr[right] = arr[right], arr[left]

    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
