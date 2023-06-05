from typing import List
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
    return recurse(
        preorder,
        inorder,
        node_to_inorder_idx,
        0,
        len(preorder) - 1,
        0,
        len(inorder) - 1)


def recurse(preorder,
            inorder,
            node_to_inorder_idx,
            preorder_left,
            preorder_right,
            inorder_left,
            inorder_right) -> Optional[BinaryTreeNode]:
    if preorder_right < preorder_left or inorder_right < inorder_left:
        return None
    data = preorder[preorder_left]
    root_inorder_idx = node_to_inorder_idx[data]
    left_tree_size = root_inorder_idx - inorder_left
    left = recurse(preorder,
                   inorder,
                   node_to_inorder_idx,
                   preorder_left + 1,
                   preorder_left + left_tree_size,
                   inorder_left,
                   root_inorder_idx - 1)
    right = recurse(preorder,
                    inorder,
                    node_to_inorder_idx,
                    preorder_left + left_tree_size + 1,
                    preorder_right,
                    root_inorder_idx + 1,
                    inorder_right)
    return BinaryTreeNode(data, left, right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
