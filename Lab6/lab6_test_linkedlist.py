# SYSC 2100 Winter 2023 Lab 6: Unit tests.

import unittest

from lab6_linkedlist import LinkedList

# The following classes test the LinkedList methods developed during Lab 6.


class ContainsTestCase(unittest.TestCase):
    """Test __contains__ (Exercise 1)."""

class EqTestCase(unittest.TestCase):
    """Test __eq__ (Exercise 2)."""

class DelTestCase(unittest.TestCase):
    """Test __delitem__ (Exercise 3)."""

    def test_del1(self):
        """Test an index that is too large."""
        lst = LinkedList([1, 4, 3, 6])
        with self.assertRaises(IndexError):
            del lst[4]

    def test_del2(self):
        """Test a negative index."""
        lst = LinkedList([1, 4, 3, 6])
        with self.assertRaises(IndexError):
            del lst[-1]

class RemoveTestCase(unittest.TestCase):
    """Test pop (Exercise 4)."""

    def test_remove1(self):
        """Test removing an item from an empty list."""
        lst = LinkedList()
        with self.assertRaises(ValueError):
            lst.remove(10)

    def test_remove2(self):
        """Test removing an item that's not in the list."""
        lst = LinkedList([1, 4, 3, 6])
        with self.assertRaises(ValueError):
            lst.remove(10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
