"""SYSC 2100 Winter 2023 Lab 8: some unit tests for Exercises 1, 2, 3 and 7."""

import unittest

from lab8_binarytree import BinaryTree, \
    build_10_20_30, build_binary_tree, build_perfect_binary_tree


class Build_10_20_30_TestCase(unittest.TestCase):
    """Test build_10_20_30. (Exercise 1)."""

    def test_1(self):
        tree = build_10_20_30()
        # Check the root node
        self.assertEqual(tree._root.x, 10)

        # Check the root's left child
        left_child = tree._root.left
        self.assertEqual(left_child.x, 20)
        self.assertIsNone(left_child.left)
        self.assertIsNone(left_child.right)

        # Check the root's right child
        right_child = tree._root.right
        self.assertEqual(right_child.x, 30)
        self.assertIsNone(right_child.left)
        self.assertIsNone(right_child.right)


class Build_Binary_Tree_TestCase(unittest.TestCase):
    """Test build_binary_tree (Exercise 2)."""

    def test_build_binary_tree(self):
        tree = build_binary_tree()

        # Check that the root node's payload is 1
        self.assertEqual(tree._root.x, 1)

        # Check that the left child's payload is 2
        self.assertEqual(tree._root.left.x, 2)

        # Check that the right child's payload is 3
        self.assertEqual(tree._root.right.x, 3)

        # Check that the left child's left child's payload is 4
        self.assertEqual(tree._root.left.left.x, 4)

        # Check that the left child's right child's payload is 5
        self.assertEqual(tree._root.left.right.x, 5)

        # Check that the right child's left child's payload is 6
        self.assertEqual(tree._root.right.left.x, 6)

        # Check that the right child's right child's payload is 7
        self.assertEqual(tree._root.right.right.x, 7)


class Build_Perfect_Binary_Tree_TestCase(unittest.TestCase):
    """Test build_perfect_binary_tree. (Exercise 3)."""

    def test_build_perfect_binary_tree(self):
        tree = build_perfect_binary_tree(2)

        # Check the root node
        self.assertEqual(tree._root.x, 1)

        # Check the left subtree
        left_subtree = tree._root.left
        self.assertEqual(left_subtree.x, 2)
        self.assertEqual(left_subtree.left.x, 4)
        self.assertEqual(left_subtree.right.x, 5)

        # Check the right subtree
        right_subtree = tree._root.right
        self.assertEqual(right_subtree.x, 3)
        self.assertEqual(right_subtree.left.x, 6)
        self.assertEqual(right_subtree.right.x, 7)


class CountTestCase(unittest.TestCase):
    """Test the count method (Exercise 7)."""


if __name__ == '__main__':
    unittest.main(verbosity=2)
