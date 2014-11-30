import unittest
import balancing_tree
import random


class test_BalancingBinarySearchTree(unittest.TestCase):

    def test_with_random_values(self):

        for each_pass in range(0, 100):

            random_tree = balancing_tree.BalancingBinarySearchTree()

            for each_new_node in range(5, random.randint(10, 100)):
                random_tree.insert(random.randint(0, 100))
            sorted_tree_contents = random_tree.in_order_print(
                random_tree.root_node, returning=True)

            for each_node_index in range(0, (len(sorted_tree_contents) - 1)):
                assert (sorted_tree_contents[each_node_index]
                        <= sorted_tree_contents[(each_node_index + 1)])

    def setUp(self):

        self.worst_balancing_tree = balancing_tree.BalancingBinarySearchTree()
        for each_integer in range(0, 20):
            self.worst_balancing_tree.insert(each_integer)

        self.empty_balancing_tree = balancing_tree.BalancingBinarySearchTree()

        with self.assertRaises(TypeError):
            balancing_tree.BalancingBinarySearchTree("Not valid")

        with self.assertRaises(TypeError):
            balancing_tree.BalancingBinarySearchTree([55, 2, 1])

        with self.assertRaises(TypeError):
            balancing_tree.BalancingBinarySearchTree(42)

        with self.assertRaises(TypeError):
            balancing_tree.BalancingBinarySearchTree(None)

    def test_insert(self):

        self.setUp()

        with self.assertRaises(TypeError):
            self.empty_balancing_tree.insert("Not valid")

        with self.assertRaises(TypeError):
            self.empty_balancing_tree.insert([10, 11, 12, 13])

        with self.assertRaises(TypeError):
            self.empty_balancing_tree.insert(10, 11, 12, 13)

        with self.assertRaises(TypeError):
            self.empty_balancing_tree.insert(None)

        with self.assertRaises(TypeError):
            self.worst_balancing_tree.insert("Not valid")

        with self.assertRaises(TypeError):
            self.worst_balancing_tree.insert([10, 11, 12, 13])

        with self.assertRaises(TypeError):
            self.worst_balancing_tree.insert(10, 11, 12, 13)

        with self.assertRaises(TypeError):
            self.worst_balancing_tree.insert(None)

    # Decided to save some typing by borrowing constants
    # from Charlie's repo. Asked him before he left if
    # I could use his repo to help, and this is more of
    # a time-intensive thing than a conceptual thing...
    # If this is unacceptable please let me know.

    def test_insert(self):

        self.setUp()

        self.empty_balancing_tree.insert(0)
        self.empty_balancing_tree.insert(-2)
        self.empty_balancing_tree.insert(2)
        self.empty_balancing_tree.insert(-1)
        self.empty_balancing_tree.insert(3)
        self.empty_balancing_tree.insert(-3)
        self.empty_balancing_tree.insert(3)
        self.empty_balancing_tree.insert(1)

        assert self.empty_balancing_tree.root_node.value == 0
        assert self.empty_balancing_tree.root_node.left.value == -2
        assert self.empty_balancing_tree.root_node.left.left.value == -3
        assert self.empty_balancing_tree.root_node.left.right.value == -1
        assert self.empty_balancing_tree.root_node.right.value == 2
        assert self.empty_balancing_tree.root_node.right.right.value == 3
        assert self.empty_balancing_tree.root_node.right.left.value == 1

    def test_balance(self):

        self.setUp()

        with self.assertRaises(AttributeError):
            assert self.empty_balancing_tree.balance() == 0

        assert self.worst_balancing_tree.balance() == -1

    def test_depth(self):

        self.setUp()

        assert self.empty_balancing_tree.depth() == 0
        # Down from 20 without AVL balancing!
        assert self.worst_balancing_tree.depth() == 5

    def test_size(self):

        self.setUp()

        assert self.empty_balancing_tree.size() == 0
        assert self.worst_balancing_tree.size() == 20


    def test_contains(self):

        self.setUp()

        assert self.empty_balancing_tree.contains(0) is False
        assert self.empty_balancing_tree.contains(1) is False
        assert self.empty_balancing_tree.contains(-1) is False

        self.empty_balancing_tree.insert(0)
        self.empty_balancing_tree.insert(1)
        self.empty_balancing_tree.insert(-1)
        self.empty_balancing_tree.insert(2)
        self.empty_balancing_tree.insert(-2)

        assert self.empty_balancing_tree.contains(-1) is True
        assert self.empty_balancing_tree.contains(0) is True

        with self.assertRaises(ValueError):
            assert self.empty_balancing_tree.contains(None) is False

    def test_delete(self):

        self.setUp()

        with self.assertRaises(Exception):
            self.empty_balancing_tree.delete()

        with self.assertRaises(Exception):
            self.worst_balancing_tree.delete()

        assert self.worst_balancing_tree.contains(11) is True
        assert self.worst_balancing_tree.contains(2) is True
        assert self.worst_balancing_tree.contains(19) is True

        assert self.worst_balancing_tree.contains(10) is True
        assert self.worst_balancing_tree.contains(1) is True
        assert self.worst_balancing_tree.contains(18) is True

        self.worst_balancing_tree.delete(10)
        self.worst_balancing_tree.delete(1)
        self.worst_balancing_tree.delete(18)

        assert self.worst_balancing_tree.contains(11) is True
        assert self.worst_balancing_tree.contains(2) is True
        assert self.worst_balancing_tree.contains(19) is True

        assert self.worst_balancing_tree.contains(10) is False
        assert self.worst_balancing_tree.contains(1) is False
        assert self.worst_balancing_tree.contains(18) is False

        self.empty_balancing_tree.insert(0)
        self.empty_balancing_tree.insert(1)
        self.empty_balancing_tree.insert(-1)
        self.empty_balancing_tree.insert(2)
        self.empty_balancing_tree.insert(-2)

        assert self.empty_balancing_tree.contains(-1) is True
        assert self.empty_balancing_tree.contains(0) is True

        self.empty_balancing_tree.delete(-1)


unittest.main()
