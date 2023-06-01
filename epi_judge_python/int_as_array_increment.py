from typing import List

from test_framework import generic_test


def plus_one(arr: List[int]) -> List[int]:
    i = len(arr) - 1
    while i >= 0:
        res = arr[i] + 1
        if res < 10:
            arr[i] = res
            break
        arr[i] = 0
        i -= 1

    if i < 0 and arr[0] == 0:
        arr[0] = 1
        arr.append(0)

    return arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
