from heapq import *
from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    def __init__(self):
        self.storage = []

    def empty(self) -> bool:
        return len(self.storage) == 0

    def max(self) -> int:
        return self.storage[-1][1]

    def pop(self) -> int:
        return self.storage.pop()[0]

    def push(self, x: int) -> None:
        max_value = x
        if not self.empty():
            max_value = max(x, self.max())
        self.storage.append((x, max_value))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
