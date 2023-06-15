from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(list_node: ListNode) -> Optional[ListNode]:
    return recurse(list_node)


def recurse(list_node: ListNode):
    if not list_node or not list_node.next:
        return list_node

    prev = None
    slow = list_node
    fast = list_node

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None

    l1, l2 = list_node, slow
    return merge(recurse(l1), recurse(l2))


def merge(l1: ListNode, l2: ListNode):
    if l1.data <= l2.data:
        head, curr = l1, l1
        l1 = l1.next
    else:
        head, curr = l2, l2
        l2 = l2.next

    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        else:
            curr.next = l2
            curr = curr.next
            l2 = l2.next

    curr.next = l1 or l2

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
