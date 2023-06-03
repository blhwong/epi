from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(head: ListNode, k: int) -> Optional[ListNode]:
    prev = None
    p1 = head
    p2 = head
    for _ in range(k):
        p2 = p2.next

    while p2 is not None:
        prev = p1
        p1 = p1.next
        p2 = p2.next

    if prev is not None:
        prev.next = p1.next
    else:
        head = p1.next

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
