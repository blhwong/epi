from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.first, self.last = 0, 0
        self.count = 0
        self.storage = [0] * capacity

    def enqueue(self, x: int) -> None:
        if self.count >= len(self.storage):
            reordered = self.storage[self.first:] + self.storage[:self.first]
            new_partition = [0] * self.count
            self.storage = reordered + new_partition
            self.first, self.last = 0, self.count

        self.storage[self.last] = x
        self.last = (self.last + 1) % len(self.storage)
        self.count += 1

    def dequeue(self) -> int:
        x = self.storage[self.first]
        self.first = (self.first + 1) % len(self.storage)
        self.count -= 1
        return x

    def size(self) -> int:
        return self.count


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
