from test_framework import generic_test


def reverse_bits(x: int) -> int:
    ans = 0
    for _ in range(64):
        ans <<= 1
        if x & 1 != 0:
            ans += 1
        x >>= 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
