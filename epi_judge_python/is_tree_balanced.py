from typing import Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return traverse(tree)[1]


def traverse(curr: BinaryTreeNode) -> Tuple[int, bool]:
    if curr is None:
        return -1, True
    left_height, left_balanced = traverse(curr.left)
    right_height, right_balanced = traverse(curr.right)
    height = 1 + max(left_height, right_height)
    balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
    return height, balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
