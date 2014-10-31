import unittest
import bst
import random


class test_BinarySearchTree(unittest.TestCase):

    def setUp(self):

        self.worst_bst = bst.BinarySearchTree()
        for each_integer in range(0, 20):
            self.worst_bst.insert(each_integer)

        self.empty_bst = bst.BinarySearchTree()

        with self.assertRaises(TypeError):
            bst.BinarySearchTree("Not valid")

        with self.assertRaises(TypeError):
            bst.BinarySearchTree([55, 2, 1])

        with self.assertRaises(TypeError):
            bst.BinarySearchTree(42)

        with self.assertRaises(TypeError):
            bst.BinarySearchTree(None)

    def test_insert(self):

        self.setUp()

        with self.assertRaises(TypeError):
            self.empty_bst.insert("Not valid")

        with self.assertRaises(TypeError):
            self.empty_bst.insert([10, 11, 12, 13])

        with self.assertRaises(TypeError):
            self.empty_bst.insert(10, 11, 12, 13)

        with self.assertRaises(TypeError):
            self.empty_bst.insert(None)

        with self.assertRaises(TypeError):
            self.worst_bst.insert("Not valid")

        with self.assertRaises(TypeError):
            self.worst_bst.insert([10, 11, 12, 13])

        with self.assertRaises(TypeError):
            self.worst_bst.insert(10, 11, 12, 13)

        with self.assertRaises(TypeError):
            self.worst_bst.insert(None)

    # Decided to save some typing by borrowing constants
    # from Charlie's repo. Asked him before he left if
    # I could use his repo to help, and this is more of
    # a time-intensive thing than a conceptual thing...
    # If this is unacceptable please let me know.

    def test_insert(self):

        self.setUp()

        self.empty_bst.insert(0)
        self.empty_bst.insert(-2)
        self.empty_bst.insert(2)
        self.empty_bst.insert(-1)
        self.empty_bst.insert(3)
        self.empty_bst.insert(-3)
        self.empty_bst.insert(3)
        self.empty_bst.insert(1)

        assert self.empty_bst.root_node.value == 0
        assert self.empty_bst.root_node.left.value == -2
        assert self.empty_bst.root_node.left.left.value == -3
        assert self.empty_bst.root_node.left.right.value == -1
        assert self.empty_bst.root_node.right.value == 2
        assert self.empty_bst.root_node.right.right.value == 3
        assert self.empty_bst.root_node.right.left.value == 1

    def test_balance(self):

        self.setUp()

        assert self.empty_bst.balance() == 0
        assert self.worst_bst.balance() == -19

    def test_depth(self):

        self.setUp()

        assert self.empty_bst.depth() == 0
        assert self.worst_bst.depth() == 20

    def test_size(self):

        self.setUp()

        assert self.empty_bst.size() == 0
        assert self.worst_bst.size() == 20


    def test_contains(self):

        self.setUp()

        assert self.empty_bst.contains(0) is False
        assert self.empty_bst.contains(1) is False
        assert self.empty_bst.contains(-1) is False

        self.empty_bst.insert(0)
        self.empty_bst.insert(1)
        self.empty_bst.insert(-1)
        self.empty_bst.insert(2)
        self.empty_bst.insert(-2)

        assert self.empty_bst.contains(-1) is True
        assert self.empty_bst.contains(0) is True

        with self.assertRaises(ValueError):
            assert self.empty_bst.contains(None) is False

    def test_delete(self):

        self.setUp()

        with self.assertRaises(Exception):
            self.empty_bst.delete()

        with self.assertRaises(Exception):
            self.worst_bst.delete()

        assert self.worst_bst.contains(11) is True
        assert self.worst_bst.contains(2) is True
        assert self.worst_bst.contains(19) is True

        assert self.worst_bst.contains(10) is True
        assert self.worst_bst.contains(1) is True
        assert self.worst_bst.contains(18) is True

        self.worst_bst.delete(10)
        self.worst_bst.delete(1)
        self.worst_bst.delete(18)

        assert self.worst_bst.contains(11) is True
        assert self.worst_bst.contains(2) is True
        assert self.worst_bst.contains(19) is True

        assert self.worst_bst.contains(10) is False
        assert self.worst_bst.contains(1) is False
        assert self.worst_bst.contains(18) is False

        self.empty_bst.insert(0)
        self.empty_bst.insert(1)
        self.empty_bst.insert(-1)
        self.empty_bst.insert(2)
        self.empty_bst.insert(-2)

        assert self.empty_bst.contains(-1) is True
        assert self.empty_bst.contains(0) is True

        self.empty_bst.delete(-1)



unittest.main()