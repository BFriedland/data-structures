
import unittest

import priority_queue


class test_PriorityQueue(unittest.TestCase):

    def setUp(self):

        self.empty_max_priority_queue = priority_queue.PriorityQueue(
            max_or_min="max")

        # Test the supplied_iterable kwarg:
        def craft_iterable():

            # 10, 20, 30, 40, 50, 60, 70, 80
            for each_number in range(10, 81, 10):
                import random
                random_value = random.randint(400, 500)
                yield random_value, each_number

        self.populated_max_priority_queue = priority_queue.PriorityQueue(
            max_or_min="max",
            supplied_iterable=craft_iterable())

    # def test_PriorityQueue_parameters(self):

    #     with self.assertRaises(Exception):
    #         priority_queue.PriorityQueue(supplied_iterable=423515342282)

    #     # Just call do_something(), and if an exception gets raised,
    #     # the test automatically fails.
    #     # This is also the reason why assertDoesNotRaise() does not exist.
    #     # Reference:
    #     # http://stackoverflow.com/questions/6181555/
    #     #   pass-a-unit-test-if-an-exception-isnt-thrown
    #     priority_queue.PriorityQueue()

    #     with self.assertRaises(Exception):
    #         priority_queue.PriorityQueue(
    #             supplied_iterable="Test string 12()3)\45")

    # def test_insert(self):
    #     ''' .insert() puts a new value into the queue,
    #     maintaining the order of priorities. '''

    #     self.setUp()

    #     self.empty_max_priority_queue.insert("value", 90)
    #     self.assertEquals(self.empty_max_priority_queue.the_array[1].priority,
    #                       90)

    #     self.populated_max_priority_queue.insert("value", 90)
    #     self.assertEquals(self.populated_max_priority_queue.the_array[1].priority,
    #                       90)

    # def test_pop(self):
    #     ''' .pop() removes the "top" value in the queue,
    #     maintaining the order of priorities. '''

    #     self.setUp()
    #     # Shortened reference for PEP 8 compliance:
    #     priority_queue_array = self.populated_max_priority_queue.the_array

    #     with self.assertRaises(IndexError):
    #         self.empty_max_priority_queue.pop()

    #     popped_number_for_populated_priority_queue = \
    #         self.populated_max_priority_queue.insert("value", 55)

    #     self.assertEquals(priority_queue_array[1].priority, 80)

    #     # Iterate through the array to test the order of priorities on all.
    #     for each_node in range(1, len(priority_queue_array) / 2):

    #         # I can't believe this method worked on the first run.
    #         self.assertEquals((priority_queue_array[each_node].priority
    #                            >= priority_queue_array[(each_node * 2)].priority), True)
    #         self.assertEquals((priority_queue_array[each_node]
    #                            >= priority_queue_array[((each_node * 2) + 1)].priority), False)

    #     with self.assertRaises(TypeError):
    #         self.empty_max_priority_queue.pop(100)

    # def test_the_actual_order_of_priority(self):

    #     self.setUp()

    #     self.assertEquals(self.populated_max_priority_queue.the_array[1].priority,
    #                       80)

    #     # Shortened reference for PEP 8 compliance:
    #     priority_queue_array = self.populated_max_priority_queue.the_array

    #     # Iterate through the array to test the order of priorities on all.
    #     for each_node in range(1, len(priority_queue_array) / 2):

    #         self.assertEquals((priority_queue_array[each_node].priority
    #                            >= priority_queue_array[(each_node * 2)].priority), True)
    #         self.assertEquals((priority_queue_array[each_node].priority
    #                            >= priority_queue_array[((each_node * 2) + 1)].priority), True)

    # def test_peek(self):

    #     self.setUp()

    #     self.assertEquals(self.populated_max_priority_queue.peek().priority, 80)

    #     self.empty_max_priority_queue.insert("value", 90)
    #     self.assertEquals(self.empty_max_priority_queue.peek().priority, 90)

    #     self.empty_max_priority_queue.insert("value", 10)
    #     self.assertEquals(self.empty_max_priority_queue.peek().priority, 90)

    #     self.empty_max_priority_queue.insert("value", 100)
    #     self.assertEquals(self.empty_max_priority_queue.peek().priority, 100)

    #     with self.assertRaises(TypeError):
    #         self.empty_max_priority_queue.peek(100).priority

    def test__down_propagate_priority_order(self):

        self.setUp()

        self.empty_max_priority_queue.the_array.append(
            priority_queue.Node(1, 10))
        #self.empty_max_priority_queue.the_array.append(
        #    priority_queue.Node(1, 11))
        self.empty_max_priority_queue.the_array.append(
            priority_queue.Node(1, 12))

        self.empty_max_priority_queue._down_propagate_priority_order()

        # The oddness is due to the fact that
        # a priority queue is just a binheap.
        assert self.empty_max_priority_queue.the_array[1].priority is 12
        assert self.empty_max_priority_queue.the_array[2].priority is 10
        #assert self.empty_max_priority_queue.the_array[3] is 11


unittest.main()
