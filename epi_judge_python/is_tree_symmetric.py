from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return traverse(tree, tree)


def traverse(node1: BinaryTreeNode, node2: BinaryTreeNode) -> bool:
    if node1 is None and node2 is None:
        return True
    if node1 is None and node2 is not None:
        return False
    if node1 is not None and node2 is None:
        return False
    one = node1.data == node2.data
    two = traverse(node1.left, node2.right)
    three = traverse(node1.right, node2.left)
    return one and two and three




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
