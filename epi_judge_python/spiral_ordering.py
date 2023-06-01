from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    ans = []
    n = len(square_matrix)
    size = len(square_matrix) ** 2
    i, j = 0, 0
    right, down, left, up = range(4)
    direction = right
    left_bound, right_bound = 0, n
    upper_bound, lower_bound = 1, n
    while len(ans) < size:
        ans.append(square_matrix[i][j])
        if direction == right:
            j += 1
            if j >= right_bound:
                j -= 1
                i += 1
                direction = down
                right_bound -= 1
        elif direction == down:
            i += 1
            if i >= lower_bound:
                i -= 1
                j -= 1
                direction = left
                lower_bound -= 1
        elif direction == left:
            j -= 1
            if j < left_bound:
                j += 1
                i -= 1
                direction = up
                left_bound += 1
        elif direction == up:
            i -= 1
            if i < upper_bound:
                i += 1
                j += 1
                direction = right
                upper_bound += 1

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
