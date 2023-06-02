from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    start = abs(x)
    ans = ''
    while start > 0:
        r = start % 10
        if r == 0:
            ans = '0' + ans
        elif r == 1:
            ans = '1' + ans
        elif r == 2:
            ans = '2' + ans
        elif r == 3:
            ans = '3' + ans
        elif r == 4:
            ans = '4' + ans
        elif r == 5:
            ans = '5' + ans
        elif r == 6:
            ans = '6' + ans
        elif r == 7:
            ans = '7' + ans
        elif r == 8:
            ans = '8' + ans
        elif r == 9:
            ans = '9' + ans
        start //= 10
    return ans if x >= 0 else '-' + ans


def string_to_int(s: str) -> int:
    ans = 0
    for i in range(len(s)):
        ans *= 10
        char = s[i]
        if char == '1':
            ans += 1
        elif char == '2':
            ans += 2
        elif char == '3':
            ans += 3
        elif char == '4':
            ans += 4
        elif char == '5':
            ans += 5
        elif char == '6':
            ans += 6
        elif char == '7':
            ans += 7
        elif char == '8':
            ans += 8
        elif char == '9':
            ans += 9

    return ans if s[0] != '-' else -ans


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
