# Class BinaryMaxHeap implements the priority queue interface, using a max-heap
# as the underlying data structure. (The higher the value of an element, the
# higher its priority.) The remove/delete_max operations remove the
# highest-priority element.
#
# Some code is this module was adapted from code from the Open Data Structures
# project, opendatastructures.org.
#
# This code (and the code from which it was derived) is released under a
# Creative Commons Attribution (CC BY) license. The full text of the license is
# available here:
#
# http://creativecommons.org/licenses/by/2.5/ca/
# """

__author__ = 'Damon Ricci'
__student_number__ = '101229913'

# Class BinaryMaxHeap stores a heap as a complete binary tree. Typically,
# the tree is represesented as an array, with the nodes arranged in
# breadth-first order. (The root is stored at index 0, the root's left
# child is stored at index 1, the root's right child is stored at index 2,
# etc.)

# BinaryMaxHeap uses a Python list instead of an array, because (unlike a
# fixed-capacity array), a list keeps track of the number of objects it
# contains and it will increase its capacity as required.

# Given the index of a node, we can call these functions to determine the
# index of the node's parent, left child and right child.


def left(i: int) -> int:
    """Return the index of the left child of the node at index i.
    """
    return 2 * i + 1


def right(i: int) -> int:
    """Return the index of the right child of the node at index i.
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """Return the index of the parent of the node at index i."""
    return (i - 1) // 2


class BinaryMaxHeap:

    def __init__(self, iterable=[]) -> None:
        """Initialize this BinaryMaxHeap.

        If no iterable is provided, the new BinaryMaxHeap is empty.
        Otherwise, initialize the BinaryMaxHeap by inserting the values
        provided by the iterable.
        """
        self._elems = []
        for elem in iterable:
            self.add(elem)

    def __str__(self) -> str:
        """Return a string representation of this BinaryMaxHeap."""
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "[{0}]".format(", ".join([repr(x) for x in self]))

    def __repr__(self) -> str:
        """Return the canonical string representation of this BinaryMaxHeap."""
        # For a BinaryMaxHeap object, obj, the expression eval(repr(obj))
        # returns a new BinaryMaxHeap that is identical to obj.
        return "{0}({1})".format(self.__class__.__name__, str(self))

    def __len__(self) -> int:
        """Return the number of elements in this BinaryMaxHeap."""
        return len(self._elems)

    def __iter__(self):
        """Return an iterator for this BinaryMaxHeap.

        Elements are returned in breadth-first order, starting with the
        root of the heap's tree.
        """
        # for i in range(len(self)):
        #     yield self._elems[i]

        return iter(self._elems)   # Use the list's iterator.

    def add(self, x: any) -> None:
        """Insert x in this BinaryMaxHeap."""
        self._elems.append(x)
        self._bubble_up(len(self._elems) - 1)

    def _bubble_up(self, i: int) -> None:
        """A new element was stored at index i in the heap's "array" (list).
        Bubble this element up the tree until the heap has been reformed.
        """
        p = parent(i)
        while i > 0 and self._elems[i] > self._elems[p]:
            self._elems[i], self._elems[p] = self._elems[p], self._elems[i]
            i = p
            p = parent(i)

    def remove(self) -> any:
        """Remove the largest value from this BinaryMaxHeap and return it.
        Raises IndexError if the heap is empty.
        """
        if len(self._elems) == 0:
            raise IndexError("remove: empty BinaryMaxHeap")

        x = self._elems[0]  # Largest value is in the root.
        last = self._elems.pop()

        if len(self._elems) > 0:
            self._elems[0] = last
            self._trickle_down(0)

        return x

    def _trickle_down(self, i: int) -> None:
        """Starting with the element stored at index i in the heap's array,
        trickle this element down the tree until the heap has been reformed.
        """
        while True:
            left_child = left(i)
            right_child = right(i)
            largest = i

            if left_child < len(self._elems) and self._elems[left_child] > self._elems[largest]:
                largest = left_child

            if right_child < len(self._elems) and self._elems[right_child] > self._elems[largest]:
                largest = right_child

            if largest == i:
                break

            self._elems[i], self._elems[largest] = self._elems[largest], self._elems[i]
            i = largest

    def peek(self) -> any:
        """Return, but don't remove, the largest value in this BinaryMaxHeap.
        Raises IndexError if the heap is empty.
        """
        if len(self._elems) == 0:
            raise IndexError("peek: empty BinaryMaxHeap")

        return self._elems[0]
