import binary_heap

import unittest


class test_BinaryMaxHeap(unittest.TestCase):

    def setUp(self):

        self.empty_max_binheap = binary_heap.BinaryMaxHeap()

        # Test the supplied_iterable kwarg:
        def craft_iterable():

            # 10, 20, 30, 40, 50, 60, 70, 80
            for each_number in range(10, 81, 10):
                yield each_number

        self.populated_max_binheap = binary_heap.BinaryMaxHeap(
            supplied_iterable=craft_iterable())

    def test_BinaryMaxHeap_parameters(self):

        with self.assertRaises(Exception):
            binary_heap.BinaryMaxHeap(supplied_iterable=423515342282)

        ''' Just call do_something(), and if an exception gets raised, the test automatically fails.
        This is also the reason why assertDoesNotRaise() does not exist.
        Reference:
        http://stackoverflow.com/questions/6181555/
        pass-a-unit-test-if-an-exception-isnt-thrown '''
        binary_heap.BinaryMaxHeap()

        binary_heap.BinaryMaxHeap(supplied_iterable="Test string 12()3)\45")



    def test_push(self):
        ''' .push() puts a new value into the heap,
        maintaining the heap property. '''

        self.setUp()

        self.empty_max_binheap.push(90)
        self.assertEquals(self.empty_max_binheap.the_array[1], 90)

        self.populated_max_binheap.push(90)
        self.assertEquals(self.populated_max_binheap.the_array[1], 90)

    def test_pop(self):
        ''' .pop() removes the "top" value in the heap,
        maintaining the heap property. '''

        self.setUp()
        # Shortened reference for PEP 8 compliance:
        binheap_array = self.populated_max_binheap.the_array

        with self.assertRaises(IndexError):
            self.empty_max_binheap.pop()

        popped_number_for_populated_max_binheap = \
            self.populated_max_binheap.push(55)

        self.assertEquals(binheap_array[1], 80)

        # Iterate through the array to test the heap property on everything.
        for each_node in range(0, len(binheap_array) / 2):

            # I can't believe this method worked on the first run.
            self.assertEquals((binheap_array[each_node]
                               >= binheap_array[(each_node * 2)]), True)
            self.assertEquals((binheap_array[each_node]
                               >= binheap_array[((each_node * 2) + 1)]), True)

    def test_the_actual_heap_property(self):

        self.setUp()

        self.assertEquals(self.populated_max_binheap.the_array[1], 80)

        # Shortened reference for PEP 8 compliance:
        binheap_array = self.populated_max_binheap.the_array

        # Iterate through the array to test the heap property on everything.
        for each_node in range(0, len(binheap_array) / 2):

            # I can't believe this method worked on the first run.
            self.assertEquals((binheap_array[each_node]
                               >= binheap_array[(each_node * 2)]), True)
            self.assertEquals((binheap_array[each_node]
                               >= binheap_array[((each_node * 2) + 1)]), True)

unittest.main()
