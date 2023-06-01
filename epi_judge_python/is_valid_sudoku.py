from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    for i in range(9):
        if not is_valid_row(partial_assignment, i):
            return False
        if not is_valid_column(partial_assignment, i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_square(partial_assignment, i, j):
                return False

    return True


def is_valid_row(arr, row):
    s = set()
    for i in range(9):
        num = arr[row][i]
        if num == 0:
            continue
        if num in s:
            return False
        s.add(num)
    return True


def is_valid_column(arr, column):
    s = set()
    for i in range(9):
        num = arr[i][column]
        if num == 0:
            continue
        if num in s:
            return False
        s.add(num)
    return True


def is_valid_square(arr, row, col):
    s = set()
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            num = arr[i][j]
            if num == 0:
                continue
            if num in s:
                return False
            s.add(num)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
