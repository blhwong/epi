from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(a: List[int], b: List[int]) -> List[int]:
    ans = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if not ans or (ans[-1] != a[i]):
                ans.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
