from test_framework import generic_test


def look_and_say(n: int) -> str:
    prev, curr = None, '1'
    for i in range(n):
        prev = curr
        curr = say(prev)

    return prev


def say(s: str):
    ans = ''
    count = 1
    char = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            ans += f'{count}{char}'
            count = 1
            char = s[i]

    return ans + f'{count}{char}'



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
