from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    d = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for char in s:
        if char in d:
            stack.append(d[char])
        elif len(stack) == 0 or char != stack.pop():
            return False

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
