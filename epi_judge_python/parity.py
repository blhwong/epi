from test_framework import generic_test


def parity(x: int) -> int:
    ans = 0
    while x > 0:
        if x & 1 != 0:
            ans += 1
        x >>= 1
    return 1 if ans % 2 != 0 else 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
