from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    l_dict = {}
    for char in letter_text:
        if char not in l_dict:
            l_dict[char] = 0
        l_dict[char] += 1

    m_dict = {}
    for char in magazine_text:
        if char not in m_dict:
            m_dict[char] = 0
        m_dict[char] += 1

    for char, freq in l_dict.items():
        if char not in m_dict or freq > m_dict[char]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
