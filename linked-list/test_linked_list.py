'''
Test suite for linked_list.py

Partially adapted from:
https://github.com/linsomniac/python-unittest-skeleton/blob/master/tests/test_skeleton.py

'''

import unittest
import linked_list


class test_LinkedList(unittest.TestCase):

    def setUp(self):

        # The program needs a list to test with.
        self.test_list = linked_list.LinkedList()

        for each_number in range(1, 10):
            self.test_list.insert(each_number)

    def test_LinkedList(self):

        # This feels pretty superfluous due to setUp, which appears to
        # be intended to come first, but here it is anyways.
        # For futureproofing, maybe.

        constructor_test_object = linked_list.LinkedList()
        self.assertTrue(isinstance(constructor_test_object,
                                   linked_list.LinkedList))

    def test_insert(self):

        # All insert(val) needs to do is successfully create
        # a node that holds the value.
        # This will test the Node class's basic functionality as well.
        insert_test_string = 'insert() test data'
        self.test_list.insert(insert_test_string)
        self.assertEqual(self.test_list.head.data, insert_test_string)

    def test_pop(self):

        # This will remove the test_insert() Node and return the value it had.
        pop_test_string = 'pop() test data'
        self.test_list.insert(pop_test_string)
        pop_test_return_data = self.test_list.pop()
        self.assertEqual(pop_test_return_data, pop_test_string)

    def test_size(self):

        # This will return the size of the list.
        # Should be 9, ie the range from 1 to the number before 10
        # (due to range(1, 10) in setUp() in this test suite).
        self.assertEqual(self.test_list.size(), 9)

    def test_search(self):

        search_test_string = 'search() test data'
        self.test_list.insert(search_test_string)
        # Check if the data in the Node returned by search is equal to
        # the string used to instantiate that Node.
        self.assertTrue(self.test_list.search(search_test_string).data ==
                        search_test_string)

    def test_remove(self):

        remove_test_string = 'remove() test data'

        self.test_list.insert(remove_test_string)

        node_to_remove = self.test_list.search(remove_test_string)

        self.test_list.remove(node_to_remove)

        # It will try to find the string and return None.

        self.assertEqual(self.test_list.search(remove_test_string), None)


unittest.main()
