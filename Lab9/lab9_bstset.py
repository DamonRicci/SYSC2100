# Some methods were adapted from methods in class BinarySearchTree in Lee and
# Hubbard's "Data Structures and Algorithms with Python", Section 6.5.1.

__author__ = 'Damon Ricci'
__student_number__ = '101229913'


class BSTSet:

    class _Node:
        def __init__(self, x: any, left: '_Node' = None, right: '_Node' = None) -> None:
            """Initialize this node with payload x, and links to the node's
            left and right children.
            """
            self.x = x
            self.left = left
            self.right = right

        def __iter__(self):
            """Return an iterator that performs an inorder traversal of the
            tree rooted at this node.
            """
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.x

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self, iterable=[]) -> None:
        """Initialize this BSTSet.

        If no iterable is provided, the new BSTSet is empty.
        Otherwise, initialize the BSTSet by inserting the values
        provided by the iterable.

        >>> s = BSTSet()
        >>> s
       {}

        >>> s = BSTSet([4, 2, 3, 6, 1, 5])
        >>> s
        {1, 2, 3, 4, 5, 6}
        """
        self._root = None
        self._size = 0
        for elem in iterable:
            self.add(elem)

    def __str__(self) -> str:
        """Return a string representation of this BSTSet (inorder
        traversal of the nodes).
        """
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "{{{0}}}".format(", ".join([repr(x) for x in self]))

    __repr__ = __str__

    def __len__(self) -> int:
        """Return the number of elements in this BSTSet."""
        return self.size

    def __iter__(self):
        """Return an iterator that performs an inorder traversal of the nodes
        in this BSTSet.
        """
        if self._root is not None:
            return self._root.__iter__()
        else:
            # The tree is empty, so use an empty list's iterator
            # as the tree's iterator.
            return iter([])

    # Exercise 3

    def __contains__(self, x: any):
        """Return True if x is in this BSTSet; otherwise False.

        >>> s = BSTSet([1, 4, 3, 6])
        >>> 4 in s
        True
        >>> 7 in s
        False
        """
        return self._contains(self._root, x)

    def _contains(self, node: 'BSTSet._Node', x: any) -> bool:
        if node is None:
            return False
        elif x == node.x:
            return True
        elif x < node.x:
            return self._contains(node.left, x)
        else:
            return self._contains(node.right, x)

    # Exercise 4

    def __eq__(self, other: 'BSTSet') -> bool:
        """Return True if self is equal to the BSTSet referred to by other;
        otherwise return False.

        >>> s1 = BSTSet([1, 2, 3])
        >>> s2 = BSTSet([3, 2, 1])
        >>> s1 == s2
        True

        >>> s1 = BSTSet([1, 2, 3])
        >>> s2 = BSTSet([4, 5, 6])
        >>> s1 == s2
        False
        """
        if not isinstance(other, BSTSet):
            return False
        if len(self) != len(other):
            return False
        return all(item in other for item in self)

    # Exercise 5

    def __or__(self, other: 'BSTSet') -> 'BSTSet':
        """Return a new BSTSet containing the union of self and other.

        Raises TypeError if other is not a BSTSet.

        >>> s1 = BSTSet([1, 3, 5])
        >>> s2 = BSTSet([3, 4, 5, 6])
        >>> s3 = s1 | s2
        >>> repr(s3)
        '{1, 3, 4, 5, 6}'
        """
        if not isinstance(other, BSTSet):
            raise TypeError("unsupported operand type for |")
        new_set = BSTSet(self)
        for item in other:
            new_set.add(item)
        return new_set

    # Exercise 2

    def add(self, x: any) -> None:
        """Insert x into this BSTSet.

        >>> s = BSTSet([1, 4, 3, 6])
        >>> s.add(3)
        >>> s.add(7)
        >>> s
        {1, 3, 4, 6, 7}
        """
        self._root = self._add(self._root, x)

        def _add(self, node: 'BSTSet._Node', x: any) -> 'BSTSet._Node':
            if node is None:
                self._size += 1
                return self._Node(x)
            elif x < node.x:
                node.left = self._add(node.left, x)
            elif x > node.x:
                node.right = self._add(node.right, x)
            return node

    def size(self) -> int:
        """Return the number of elements in this BSTSet."""

        def _size(node: 'BSTSet._Node') -> int:
            """Return the number of nodes in the tree rooted at node."""
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self._root)
