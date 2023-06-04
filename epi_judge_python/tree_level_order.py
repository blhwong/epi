from collections import deque
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    ans = []
    if tree is None:
        return ans
    q = deque()
    q.append(tree)

    while len(q) > 0:
        level = []
        for _ in range(len(q)):
            curr = q.popleft()
            level.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        ans.append(level)

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
