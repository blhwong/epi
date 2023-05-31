from test_framework import generic_test


def power(x: float, y: int) -> float:
    dp = [-1] * (abs(y) + 1)
    if y < 0:
        return recurse(1/x, -y, dp)
    return recurse(x, y, dp)


def recurse(x: float, y: int, dp) -> float:
    if y == 0:
        return 1
    if y == 1:
        return x
    if dp[y] > -1:
        return dp[y]
    left = y // 2
    right = y - y // 2
    dp[y] = recurse(x, left, dp) * recurse(x, right, dp)
    return dp[y]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
