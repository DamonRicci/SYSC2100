# An implementation of ADT Map that uses a binary search tree as the
# underlying data structure.

# Some methods were adapted from methods in class BinarySearchTree in Lee and
# Hubbard's "Data Structures and Algorithms with Python", Section 6.5.1.

__author__ = 'Damon Ricci'
__student_number__ = '101229913'


class BSTMap:

    class _Node:
        def __init__(self, key: any, value: any, left: '_Node' = None, right: '_Node' = None) -> None:
            """Initialize a node containing a key, the value associated with
            the key, and links to the node's left and right children.
            """
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __iter__(self):
            """Return an iterator that performs an inorder traversal of the
            tree rooted at this node, returning the keys.
            """
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.key

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self, iterable=[]) -> None:
        """Initialize this BSTMap.

        If no iterable is provided, the map is empty.
        Otherwise, initialize the map by inserting the key/value pairs
        provided by the iterable.

        Precondition: the iterable is a sequence of tuples, with each tuple
        containing one (key, value) pair.

        >>> map = BSTMap()
        >>> map
        {}

        # In this example each key/value pair is a tuple containing a
        # 6-digit student number (an int) and that student's letter grade
        # (a str).

        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')])
        >>> grades
        {101156: 'A+', 111537: 'A+', 127118: 'B', }
        """
        self._root = None

        # Number of entries in the map; i.e., the number of key/value pairs.
        self._num_entries = 0

        for key, value in iterable:
            self[key] = value  # updates self._num_entries

    def __str__(self) -> str:
        """Return a string representation of this BSTMap (inorder traversal of
        the nodes), using the format: "{key_1: value_1, key_2: value_2, ...}"

        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')])
        >>> str(grades)
        "{101156: 'A+', 111537: 'A+', 127118: 'B'}"
        """
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "{{{0}}}".format(", ".join([repr(key) + ': ' + repr(self[key]) for key in self]))

    __repr__ = __str__

    def __iter__(self):
        """Return an iterator that performs an inorder traversal of the nodes
        in this BSTMap, returning the keys.
        """
        if self._root is not None:
            return self._root.__iter__()
        else:
            # The tree is empty, so use an empty list's iterator
            # as the tree's iterator.
            return iter([])

    def __len__(self) -> int:
        """Return the number of key/value pairs in the map."""
        return self._num_entries

    def __getitem__(self, key: any) -> any:
        """Return the value associated with the given key. If the key is not
        in the map, raise a KeyError.
        """
        def _find(node: '_Node') -> '_Node':
            if node is None or node.key == key:
                return node
            elif key < node.key:
                return _find(node.left)
            else:
                return _find(node.right)

        node = _find(self._root)
        if node:
            return node.value
        else:
            raise KeyError(key)

    def __setitem__(self, key: any, value: any) -> None:
        """Insert or update a key/value pair in the map."""
        def _insert(node: '_Node') -> '_Node':
            if node is None:
                self._num_entries += 1
                return self._Node(key, value)

            if key == node.key:
                node.value = value
            elif key < node.key:
                node.left = _insert(node.left)
            else:
                node.right = _insert(node.right)

            return node

        self._root = _insert(self._root)

    def __contains__(self, key: any) -> bool:
        """Return True if the key is in the map, otherwise return False."""
        return self._find_node(self._root, key) is not None

    def get(self, key: any, default: any = None) -> any:
        """Return the value associated with the given key. If the key is not
        in the map, return the provided default value or None.
        """
        node = self._find_node(self._root, key)
        return node.value if node else default

    def _find_node(self, node: '_Node', key: any) -> '_Node':
        """Return the node containing the given key or None if the key is not
        found.
        """
        if not node or node.key == key:
            return node
        elif key < node.key:
            return self._find_node(node.left, key)
        else:
            return self._find_node(node.right, key)
