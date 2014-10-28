
# References used:
# http://domenicosolazzo.wordpress.com/2010/09/26/heapsort-a-python-example/
# http://pravin.paratey.com/posts/binary-heaps-and-priority-queues
# And, most of all:
# https://github.com/jbbrokaw/data-structures/blob/master/binheap.py


class BinaryMaxHeap():
    ''' Create a binary max heap with push(value) and pop() functions,
    optionally taking a supplied_iterable keyword parameter. '''

    def __init__(self, supplied_iterable=None):


        self.the_array = [[None]]

        if supplied_iterable is not None:
            # Preempt non-iterable input with an exception
            try:
                for each_thing in supplied_iterable:
                    self.push(each_thing)
            except:
                raise Exception("supplied_iterable must be an iterable")

    def _highest_index(self):
        # For readability later on.
        return (len(self.the_array) - 1)

    def push(self, value):
        ''' Push a new value into the bottom of the heap,
        maintaining the heap property. '''

        self.the_array.append(value)
        self._up_propagate_heap_property()

    def _up_propagate_heap_property(self):

        # It always up-propagates from the bottom.
        current_index = len(self.the_array) - 1

        parent_index = current_index // 2

        # Prevent index bound errors and only check
        # the immediately following nodes:
        while ((current_index > 1)
               and (self.the_array[current_index]
               > self.the_array[parent_index])):

            # Swapping both values at once:
            self.the_array[current_index], self.the_array[parent_index] \
                = self.the_array[parent_index], self.the_array[current_index]

            # Moving up the tree:
            current_index = parent_index
            parent_index = current_index // 2


    def pop(self):

        value_to_return = self.the_array[1]

        if len(self.the_array) > 2:
            # ... reminded of the standard functions by jbbrokaw...
            self.the_array[1] = self.the_array.pop()

        elif len(self.the_array) == 2:
            self.the_array.pop()
            # Since there is no more array, the function has to end.
            # Or else.
            return value_to_return

        # Don't disturb the None.
        else:
            raise IndexError

        # Then, make it heapy.
        self._down_propagate_heap_property()

        return value_to_return

    def _largest_valid_branch(self, current_index):

        # Legibly name the indices:
        left_branch = (2 * current_index)
        right_branch = ((2 * current_index) + 1)
        # The highest branch is farthest from the root.
        highest_branch = self._highest_index()

        # If its index overflows the list, return it first:
        if left_branch > highest_branch:
            return left_branch
        if right_branch > highest_branch:
            # Yes, do return the index at (2 * current_index) in this case.
            return left_branch
        # Otherwise, compare their values and return the greater one:
        if self.the_array[left_branch] > self.the_array[right_branch]:
            return left_branch
        else:
            return right_branch

    def _down_propagate_heap_property(self):

        # Always begin at the top when down-propagating.
        current_index = 1

        the_index_to_swap_from = self._largest_valid_branch(current_index)

        while ((the_index_to_swap_from <= self._highest_index())
               and (self.the_array[the_index_to_swap_from]
                    > self.the_array[current_index])):

            # Swapswapswap
            self.the_array[current_index],
            self.the_array[the_index_to_swap_from]         \
                = self.the_array[the_index_to_swap_from],  \
                self.the_array[current_index]

            # These variables need to be refreshed every pass.
            current_index = the_index_to_swap_from
            the_index_to_swap_from = self._largest_valid_branch(current_index)

