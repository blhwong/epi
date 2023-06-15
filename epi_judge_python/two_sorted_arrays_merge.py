from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(a: List[int], m: int, b: List[int],
                            n: int) -> None:
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[i + j + 1] = a[i]
            i -= 1
        else:
            a[i + j + 1] = b[j]
            j -= 1

    while i >= 0:
        a[i + j + 1] = a[i]
        i -= 1

    while j >= 0:
        a[i + j + 1] = b[j]
        j -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
