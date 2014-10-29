'''
Test suite for stack.py

This test suite copies heavily from test_linked_list
in my data-structures repository.

Usefully informed about the way unit tests look by:
https://github.com/linsomniac/python-unittest-skeleton/
blob/master/tests/test_skeleton.py

Note that every attribute of the Node class is tested
by the tests for the Stack class's methods.
'''

import unittest
import stack


class test_Stack(unittest.TestCase):

    def setUp(self):
        # The program needs several stacks to test with, and the unit tests
        # can modify these stacks as they go.
        # To be safe, use self.setUp on every new testing call.
        self.test_stack = stack.Stack()
        for each_number in range(1, 10):
            self.test_stack.push(each_number)
        self.test_stack_for_one_node = stack.Stack()
        self.test_stack_for_one_node.push("one node stack test data")
        self.test_stack_for_string_data = stack.Stack()
        self.test_stack_for_string_data.push("TestData")
        self.test_stack_for_string_data.push(61)
        self.test_stack_for_string_data.push("Additional Test Data")
        self.test_stack_for_no_nodes = stack.Stack()

    def test_Stack(self):
        self.setUp()
        # This feels pretty superfluous due to setUp, which appears to
        # be intended to come first, but here it is anyways.
        # We'll say it's for future-proofing.
        stack_constructor_test_object = stack.Stack()
        self.assertTrue(isinstance(stack_constructor_test_object,
                                   stack.Stack))

    def test_push(self):
        self.setUp()
        # All push(val) needs to do is successfully create
        # a node that holds the value.
        # This will test the Node class's basic functionality as well.
        push_test_string = 'push() test data'
        self.test_stack.push(push_test_string)
        self.assertEqual(self.test_stack.head.data, push_test_string)
        self.test_stack_for_one_node.push(push_test_string)
        self.assertEqual(self.test_stack_for_one_node.head.data,
                         push_test_string)
        self.test_stack_for_no_nodes.push(push_test_string)
        self.assertEqual(self.test_stack_for_no_nodes.head.data,
                         push_test_string)

    def test_pop(self):
        self.setUp()
        pop_test_string = 'pop() test data'
        self.test_stack.push(pop_test_string)
        pop_test_return_data = self.test_stack.pop()
        self.assertEqual(pop_test_return_data, pop_test_string)
        self.assertEqual(self.test_stack_for_one_node.pop(),
                         "one node stack test data")
        with self.assertRaises(Exception):
            self.test_stack_for_no_nodes.pop()


unittest.main()
