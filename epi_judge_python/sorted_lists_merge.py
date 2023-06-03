from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(l1: Optional[ListNode],
                           l2: Optional[ListNode]) -> Optional[ListNode]:
    p1 = l1
    p2 = l2
    if not l2:
        head = l1
    elif not l1:
        head = l2
    elif l1.data < l2.data:
        head = l1
    else:
        head = l2
    prev = None
    while p1 is not None and p2 is not None:
        if p1.data < p2.data:
            if prev is not None:
                prev.next = p1
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next

    while p1 is not None:
        if prev is not None:
            prev.next = p1
        prev = p1
        p1 = p1.next

    while p2 is not None:
        if prev is not None:
            prev.next = p2
        prev = p2
        p2 = p2.next

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
