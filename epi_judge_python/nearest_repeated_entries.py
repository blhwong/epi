from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    tracker = {}
    ans = float('inf')
    for i, word in enumerate(paragraph):
        if word not in tracker:
            tracker[word] = i
        else:
            ans = min(ans, i - tracker[word])
            tracker[word] = i

    return ans if ans != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
