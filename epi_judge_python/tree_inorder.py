from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    ans = []
    stack = [(tree, False)]

    while len(stack) > 0:
        curr, is_left_traversed = stack.pop()
        if curr is not None:
            if is_left_traversed:
                ans.append(curr.data)
            else:
                stack.append((curr.right, False))
                stack.append((curr, True))
                stack.append((curr.left, False))

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
