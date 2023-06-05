from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    ans = []
    prev = None
    curr = tree
    while curr is not None:
        if prev is curr.parent:
            # prev is parent
            if curr.left is not None:
                # keep going left if there is a left
                prev = curr
                curr = curr.left
            else:
                # there are no more left
                # we append result and traverse right or back to parent
                ans.append(curr.data)
                prev = curr
                curr = curr.right or curr.parent
        elif prev is curr.left:
            # we just visited left
            # we append current result then we traverse right or back to parent
            ans.append(curr.data)
            prev = curr
            curr = curr.right or curr.parent
        else:
            # both sides have been traversed so we move back up
            prev = curr
            curr = curr.parent

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
