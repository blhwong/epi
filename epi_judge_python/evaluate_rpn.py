from test_framework import generic_test


def evaluate(expression: str) -> int:
    s = []
    ops = {
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y,
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
    }
    for char in expression.split(','):
        if char in ops:
            f = ops[char]
            s.append(f(s.pop(), s.pop()))
        else:
            s.append(int(char))
    return s[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
