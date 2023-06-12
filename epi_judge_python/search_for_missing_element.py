import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(arr: List[int]) -> DuplicateAndMissing:
    x1 = 0
    x2 = 0
    for i in range(len(arr)):
        x1 ^= arr[i]
        x2 ^= i

    missing_xor_duplicate = x1 ^ x2

    mask = 1

    while missing_xor_duplicate & mask == 0:
        mask <<= 1

    one, two = 0, 0

    for i in range(len(arr)):
        if mask & i:
            one ^= i
        else:
            two ^= i

        if mask & arr[i]:
            one ^= arr[i]
        else:
            two ^= arr[i]

    for i in arr:
        if i ^ one == 0:
            return DuplicateAndMissing(one, two)

    return DuplicateAndMissing(two, one)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
