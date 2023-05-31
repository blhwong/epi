from test_framework import generic_test


def reverse(x: int) -> int:
    ans = 0
    start = abs(x)
    while start > 0:
        part = start % 10
        ans = ans * 10 + part
        start //= 10
    return ans if x > 0 else -ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
