'''
Test suite for queue.py

This test suite copies heavily from test_linked_list and test_stack
in my data-structures repository.

Usefully informed about the way unit tests look by:
https://github.com/linsomniac/python-unittest-skeleton/
blob/master/tests/test_skeleton.py

Note that every attribute of the Node class is tested
by the tests for the Queue class's methods.

'''

import unittest

# Specifically, my queue.py file.
# Python has a Queue library. Hopefully this will not result in confusion.
import queue

# Activate pytest by simply running py.test
# on the CLI in this file's directory.
# import pytest
# Not as important as I thought it'd be, and it creates a non-native
# dependency in my data-structures repo...


class test_Queue(unittest.TestCase):

    def setUp(self):

        # This tests the full functionality of
        # queue.Queue(), the queue constructor.
        # As a result, it should not be necessary
        # to make a unit test for Queue().

        # The program needs several queues to test with, and the unit tests
        # can modify these queues as they go.
        # To be safe, use self.setUp on every new testing call.
        self.test_queue = queue.Queue()

        for each_number in range(1, 10):
            self.test_queue.enqueue(each_number)

        self.test_queue_for_one_node = queue.Queue()
        self.test_queue_for_one_node.enqueue("one node queue test data")

        self.test_queue_for_string_data = queue.Queue()
        self.test_queue_for_string_data.enqueue("TestData")
        self.test_queue_for_string_data.enqueue(61)
        self.test_queue_for_string_data.enqueue("Additional Test Data")

        self.test_queue_for_no_nodes = queue.Queue()

    def test_enqueue(self):

        self.setUp()

        enqueue_test_string = 'enqueue() test data'
        self.test_queue.enqueue(enqueue_test_string)
        self.assertEqual(self.test_queue.head.data, enqueue_test_string)

        # This provides secondary testing for queue.Queue.size() as well.
        self.assertEqual(self.test_queue.number_of_created_nodes, 10)
        self.assertEqual(self.test_queue.number_of_deleted_nodes, 0)

    def test_dequeue(self):

        self.setUp()

        # This will remove the test_enqueue()ed Node and return the value it had.
        dequeue_test_string = 'dequeue() test data'
        self.test_queue.enqueue(dequeue_test_string)
        dequeue_test_return_data = self.test_queue.dequeue()
        self.assertEqual(dequeue_test_return_data, 1)

        # This provides secondary testing for queue.Queue.size() as well.
        self.assertEqual(self.test_queue.number_of_created_nodes, 10)
        self.assertEqual(self.test_queue.number_of_deleted_nodes, 1)

        self.test_queue_for_one_node.dequeue()
        self.assertEqual(self.test_queue_for_one_node.number_of_created_nodes, 1)
        self.assertEqual(self.test_queue_for_one_node.number_of_deleted_nodes, 1)

        with self.assertRaises(Exception):
            self.test_queue_for_no_nodes.dequeue()
        self.assertEqual(self.test_queue_for_no_nodes.number_of_created_nodes, 0)
        self.assertEqual(self.test_queue_for_no_nodes.number_of_deleted_nodes, 0)

        # Also check for dequeueing after enqueueing:
        with self.assertRaises(Exception):
            self.test_queue_for_one_node.dequeue()
        self.assertEqual(self.test_queue_for_one_node.number_of_created_nodes, 1)
        self.assertEqual(self.test_queue_for_one_node.number_of_deleted_nodes, 1)

        # Similar to first in this method, but we put this at the end
        # to avoid setUp() and created/deleted node count conflicts.
        self.test_queue_for_one_node.enqueue(dequeue_test_string)
        dequeue_test_return_data = self.test_queue_for_one_node.dequeue()
        self.assertEqual(dequeue_test_return_data, dequeue_test_string)

    def test_size(self):

        self.setUp()

        # This will return the size of the queue.
        # Should be 9, ie the range from 1 to the number before 10
        # (due to range(1, 10) in setUp() in this test suite).
        self.assertEqual(self.test_queue.size(), 9)
        self.assertEqual(self.test_queue_for_no_nodes.size(), 0)

        self.assertEqual(self.test_queue.size(),
                         self.test_queue.number_of_created_nodes)
        self.assertEqual(self.test_queue_for_no_nodes.size(),
                         self.test_queue_for_no_nodes.number_of_created_nodes)

        self.assertEqual(self.test_queue.number_of_deleted_nodes, 0)
        self.assertEqual(self.test_queue_for_no_nodes.number_of_deleted_nodes, 0)


unittest.main()
