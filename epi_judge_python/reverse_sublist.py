from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(head: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if head is None or start == finish:
        return head
    prev, curr = None, head
    i = 1
    while curr is not None and i < start:
        i += 1
        prev = curr
        curr = curr.next

    before_start = prev
    after_rev = curr

    while curr is not None and i <= finish:
        i += 1
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    if before_start is not None:
        before_start.next = prev
    else:
        head = prev
    after_rev.next = curr

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
