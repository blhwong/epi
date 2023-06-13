from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    d = {}
    for char in s:
        if char not in d:
            d[char] = 0
        d[char] += 1

    odds = 0
    for _, freq in d.items():
        if freq % 2 != 0:
            odds += 1

    return odds <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
