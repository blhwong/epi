from test_framework import generic_test


def hex_to_decimal(char: str) -> int:
    if char == 'A':
        num = 10
    elif char == 'B':
        num = 11
    elif char == 'C':
        num = 12
    elif char == 'D':
        num = 13
    elif char == 'E':
        num = 14
    elif char == 'F':
        num = 15
    else:
        num = int(char)

    return num


def decimal_to_hex(num: int) -> str:
    if num == 10:
        char = 'A'
    elif num == 11:
        char = 'B'
    elif num == 12:
        char = 'C'
    elif num == 13:
        char = 'D'
    elif num == 14:
        char = 'E'
    elif num == 15:
        char = 'F'
    else:
        char = str(num)

    return char


def convert_base_10(num_as_string: str, b: int) -> int:
    num = 0
    for i in range(len(num_as_string) - 1, -1, -1):
        exp = len(num_as_string) - i - 1
        char = num_as_string[i]
        if char == '-':
            break
        a = hex_to_decimal(char)
        num += a * (b ** exp)

    return num if num_as_string[0] != '-' else -num


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    b10 = convert_base_10(num_as_string, b1)

    num = abs(b10)

    if num == 0:
        return '0'

    ans = ''
    while num != 0:
        r = num % b2
        ans = decimal_to_hex(r) + ans
        num //= b2

    return ans if b10 >= 0 != '-' else '-' + ans


def recurse(num: int, base: int) -> str:
    if num == 0:
        return ''
    r = num % base
    return recurse(num // base, base) + decimal_to_hex(r)


def convert_base_recursive(num_as_string: str, b1: int, b2: int) -> str:
    b10 = convert_base_10(num_as_string, b1)

    if b10 == 0:
        return '0'

    ans = recurse(abs(b10), b2)

    return ans if b10 >= 0 else '-' + ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
