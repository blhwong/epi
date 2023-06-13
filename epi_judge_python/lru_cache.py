from collections import OrderedDict
from test_framework import generic_test
from test_framework.test_failure import TestFailure


class ListNode:

    def __init__(self, isbn, price):
        self.prev, self.next = None, None
        self.isbn = isbn
        self.price = price

    def __repr__(self):
        return f'isbn: {self.isbn} price: {self.price}'

    def detach(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev

        self.prev = None
        self.next = None


class LruCacheDoublyLinkedList:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.storage = {}
        self.head, self.tail = None, None

    def add_to_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        elif self.head.next is None:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

    def delete_node(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        node.detach()

    def lookup(self, isbn: int) -> int:
        if isbn not in self.storage:
            return -1
        node = self.storage[isbn]
        self.delete_node(node)
        self.add_to_tail(node)
        return self.storage[isbn].price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.storage:
            node = self.storage[isbn]
            self.delete_node(node)
            self.add_to_tail(node)
        else:
            node = ListNode(isbn, price)
            self.storage[isbn] = node
            self.add_to_tail(node)

        if len(self.storage) > self.capacity:
            node = self.head
            self.delete_node(node)
            del self.storage[node.isbn]

    def erase(self, isbn: int) -> bool:
        if isbn not in self.storage:
            return False

        node = self.storage[isbn]
        self.delete_node(node)
        del self.storage[isbn]

        return True


class LruCache:

    def __init__(self, capacity: int) -> None:
        self.storage = OrderedDict()
        self.capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self.storage:
            return -1
        price = self.storage.pop(isbn)
        self.storage[isbn] = price
        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.storage:
            price = self.storage.pop(isbn)
            self.storage[isbn] = price
        else:
            self.storage[isbn] = price

        if len(self.storage) > self.capacity:
            self.storage.popitem(last=False)

    def erase(self, isbn: int) -> bool:
        if isbn not in self.storage:
            return False
        self.storage.pop(isbn)
        return True


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
