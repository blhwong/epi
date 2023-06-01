import math
from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    ans = []
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            ans.append(i)
            for j in range(i, n + 1, i):
                primes[j] = False
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
