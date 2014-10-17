'''
Test suite for doubly_linked_list.py

This code borrows heavily from my test_linked_list.py test suite.

Note that every attribute of the Node class is tested
by the tests for the DoublyLinkedList class's methods.
'''

import unittest
import doubly_linked_list


class test_DoublyLinkedList(unittest.TestCase):

    def setUp(self):

        self.test_list = doubly_linked_list.DoublyLinkedList()

        for each_number in range(1, 10):
            self.test_list.insert(each_number)

        self.test_list_for_one_node = doubly_linked_list.DoublyLinkedList()
        self.test_list_for_one_node.insert("one node list test data")

        self.test_list_for_string_data = doubly_linked_list.DoublyLinkedList()
        self.test_list_for_string_data.insert('TestData')
        self.test_list_for_string_data.insert(61)
        self.test_list_for_string_data.insert("Additional Test Data")

        self.test_list_for_no_nodes = doubly_linked_list.DoublyLinkedList()

    def test_DoublyLinkedList(self):

        self.setUp()

        # This feels pretty superfluous due to setUp, which appears to
        # be intended to come first, but here it is anyways.
        # We'll say it's for future-proofing.

        constructor_test_object = doubly_linked_list.DoublyLinkedList()
        self.assertTrue(isinstance(constructor_test_object,
                                   doubly_linked_list.DoublyLinkedList))

    def test_insert(self):

        self.setUp()

        # All insert(val) needs to do is successfully create
        # a node that holds the value.
        # This will test the Node class's basic functionality as well.
        insert_test_string = 'insert() test data'
        self.test_list.insert(insert_test_string)
        self.assertEqual(self.test_list.head.data, insert_test_string)

    def test_append(self):

        self.setUp()

        append_test_string = 'append() test data'
        self.test_list.append(append_test_string)
        self.assertEqual(self.test_list.tail.data, append_test_string)

        append_test_number = 999
        self.test_list.append(append_test_number)
        self.assertEqual(self.test_list.tail.data, append_test_number)

        self.test_list_for_no_nodes.append(append_test_string)
        self.assertEqual(self.test_list_for_no_nodes.tail.data,
                         append_test_string)

    def test_pop(self):

        self.setUp()

        for each_number in range(9, 0, -1):

            pop_test_return_data = self.test_list.pop()
            self.assertEqual(pop_test_return_data, each_number)

        pop_test_string = 'pop() test data'
        self.test_list.insert(pop_test_string)

        pop_test_return_data = self.test_list.pop()
        self.assertEqual(pop_test_return_data, pop_test_string)

        with self.assertRaises(Exception):
            self.test_list_for_no_nodes.pop()

        self.test_list_for_no_nodes.insert(pop_test_string)
        self.assertEqual(self.test_list_for_no_nodes.pop(),
                         pop_test_string)
        self.assertEqual(self.test_list_for_no_nodes.head, None)
        self.assertEqual(self.test_list_for_no_nodes.tail, None)






        pop_test_string = 'pop() test data'
        self.test_list.insert(pop_test_string)
        pop_test_return_data = self.test_list.pop()
        self.assertEqual(pop_test_return_data, pop_test_string)

        with self.assertRaises(Exception):
            self.test_list_for_no_nodes.shift()

    def test_shift_method(self):

        # I discovered that unittest seems to use test_shift() as a function
        # that it feeds an argument.
        # I had no calls to test_shift() whatsoever, so I think this
        # might have been overwriting an interal function call
        # for the module...
        # Kind of spooky to stumble into it like that.
        # How often will I find situations like this in the wild?

        self.setUp()

        for each_number in range(1, 10):

            shift_test_return_data = self.test_list.shift()
            self.assertEqual(shift_test_return_data, each_number)

        shift_test_string = 'shift() test data'
        self.test_list.append(shift_test_string)

        shift_test_return_data = self.test_list.shift()
        self.assertEqual(shift_test_return_data, shift_test_string)

        with self.assertRaises(Exception):
            self.test_list_for_no_nodes.shift()

        self.test_list_for_no_nodes.append(shift_test_string)
        self.assertEqual(self.test_list_for_no_nodes.shift(),
                         shift_test_string)
        self.assertEqual(self.test_list_for_no_nodes.head, None)
        self.assertEqual(self.test_list_for_no_nodes.tail, None)

    def test_remove(self):

        self.setUp()

        remove_test_string = 'remove() test data'

        self.test_list.insert(remove_test_string)
        self.test_list.remove(remove_test_string)

        self.test_list.append(remove_test_string)
        self.test_list.remove(remove_test_string)

        test_string_for_no_nodes = "This test string is for the empty list."

        with self.assertRaises(Exception):
            self.test_list_for_no_nodes.remove(test_string_for_no_nodes)


unittest.main()
