from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(head: ListNode) -> Optional[ListNode]:
    if head is None:
        return head
    even_head, odd_head = None, None
    even_prev, odd_prev = None, None

    curr = head

    i = 0

    while curr is not None:
        if i % 2 == 0:
            if even_head is None:
                even_head = curr
                even_prev = curr
            else:
                even_prev.next = curr
                even_prev = curr
        else:
            if odd_head is None:
                odd_head = curr
                odd_prev = curr
            else:
                odd_prev.next = curr
                odd_prev = curr

        curr = curr.next
        i += 1

    if even_prev:
        even_prev.next = odd_head
    if odd_prev:
        odd_prev.next = None

    return even_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
