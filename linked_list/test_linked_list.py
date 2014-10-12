'''
Test suite for linked_list.py

Usefully informed about the way unit tests look by:
https://github.com/linsomniac/python-unittest-skeleton/
blob/master/tests/test_skeleton.py

Note that every attribute of the Node class is tested
by the tests for the LinkedList class's methods.

'''

import unittest
import linked_list


class test_LinkedList(unittest.TestCase):

    def setUp(self):

        # The program needs several lists to test with, and the unit tests
        # can modify these lists as they go.
        # To be safe, use self.setUp on every new testing call.
        self.test_list = linked_list.LinkedList()

        for each_number in range(1, 10):
            self.test_list.insert(each_number)

        self.test_list_for_one_node = linked_list.LinkedList()
        self.test_list_for_one_node.insert("one node list test data")

        self.test_list_for_string_data = linked_list.LinkedList()
        self.test_list_for_string_data.insert("TestData")
        self.test_list_for_string_data.insert(61)
        self.test_list_for_string_data.insert("Additional Test Data")

        self.test_list_for_no_nodes = linked_list.LinkedList()

    def test_LinkedList(self):

        self.setUp()

        # This feels pretty superfluous due to setUp, which appears to
        # be intended to come first, but here it is anyways.
        # We'll say it's for future-proofing.

        constructor_test_object = linked_list.LinkedList()
        self.assertTrue(isinstance(constructor_test_object,
                                   linked_list.LinkedList))

    def test_insert(self):

        self.setUp()

        # All insert(val) needs to do is successfully create
        # a node that holds the value.
        # This will test the Node class's basic functionality as well.
        insert_test_string = 'insert() test data'
        self.test_list.insert(insert_test_string)
        self.assertEqual(self.test_list.head.data, insert_test_string)
        self.assertEqual(self.test_list.created_nodes, 10)
        self.assertEqual(self.test_list.deleted_nodes, 0)

    def test_pop(self):

        self.setUp()

        # This will remove the test_insert() Node and return the value it had.
        pop_test_string = 'pop() test data'
        self.test_list.insert(pop_test_string)
        pop_test_return_data = self.test_list.pop()
        self.assertEqual(pop_test_return_data, pop_test_string)
        self.assertEqual(self.test_list.created_nodes, 10)
        self.assertEqual(self.test_list.deleted_nodes, 1)

    def test_size(self):

        self.setUp()

        # This will return the size of the list.
        # Should be 9, ie the range from 1 to the number before 10
        # (due to range(1, 10) in setUp() in this test suite).
        self.assertEqual(self.test_list.size(), 9)
        self.assertEqual(self.test_list_for_no_nodes.size(), 0)

    def test_search(self):

        self.setUp()

        search_test_string = 'search() test data'
        self.test_list.insert(search_test_string)
        # Check if the data in the Node returned by search is equal to
        # the string used to instantiate that Node.
        self.assertTrue(self.test_list.search(search_test_string).data ==
                        search_test_string)

        test_string_for_no_nodes = "This test string is for the empty list."

        self.assertRaises(Exception, self.test_list_for_no_nodes.
                          search(test_string_for_no_nodes))

    def test_remove(self):

        self.setUp()

        remove_test_string = 'remove() test data'

        self.test_list.insert(remove_test_string)

        node_to_remove = self.test_list.search(remove_test_string)

        self.test_list.remove(node_to_remove)

        # It will try to find the string and return None.

        self.assertEqual(self.test_list.search(remove_test_string), None)
        self.assertEqual(self.test_list.created_nodes, 10)
        self.assertEqual(self.test_list.deleted_nodes, 1)

        test_string_for_no_nodes = "This test string is for the empty list."

        self.assertRaises(Exception, self.test_list_for_no_nodes.
                          remove(self.test_list_for_no_nodes.
                                 search(test_string_for_no_nodes)))

    def test___str__(self):

        self.setUp()

        self.assertEqual(str(self.test_list_for_string_data),
                         "('Additional Test Data', 61, 'TestData')")


unittest.main()
