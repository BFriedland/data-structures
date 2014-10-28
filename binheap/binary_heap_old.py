

'''
.push(): puts a new value into the heap, maintaining the heap property.
.pop(): removes the "top" value in the heap, maintaining the heap property.
'''


# For heaps you want arrays/lists.
# Building it with nodes and pointers is simply a slightly fancier binary tree.


# References used:
# http://domenicosolazzo.wordpress.com/2010/09/26/heapsort-a-python-example/
# http://pravin.paratey.com/posts/binary-heaps-and-priority-queues

class BinaryMaxHeap():
    ''' Create a binary max heap with push(value) and pop() functions,
    optionally taking a supplied_iterable keyword parameter. '''

    def __init__(self, supplied_iterable=None):
        # Important array properties to remember:
        # The "root" is at index one.
        # The deepest node created so far is at index (len(self.array) - 1)
        # The array may never have a length below one for the math to work,
        # and it will never have a length below one while the math is working.
        self.the_maxheap_array = [[None]]
        if supplied_iterable is not None:
            try:
                for each_thing in supplied_iterable:
                    self.push(each_thing)
            except:
                raise Exception("supplied_iterable must be an iterable")

    def push(self, value):
        ''' Push a new value into the bottom of the heap,
        maintaining the heap property. '''
        # Since it's zero-indexed (indices being an ordinal notion),
        # put the value we're adding at the index value
        # equal to the length of the array (a cardinal number).
        # ...
        # Which is all well and good, but we need to append a number,
        # so referencing len() turned out to be unnecessary.
        self.the_maxheap_array.append(value)
        self._up_propagate_heap_property(len(self.the_maxheap_array) - 1)

    '''
    def _up_propagate_heap_property(self):
        the_current_branch_index = (len(self.the_maxheap_array) - 1)
        while the_current_branch_index != 1:
            index_of_the_parent_branch = the_current_branch_index / 2
            if self.the_maxheap_array[index_of_the_parent_branch] \
               < self.the_maxheap_array[the_current_branch_index]:

                self.the_maxheap_array[index_of_the_parent_branch] \
                    = self.the_maxheap_array[the_current_branch_index]

                the_current_branch_index = index_of_the_parent_branch
    '''

    def _up_propagate_heap_property(self, the_current_branch_index):
        # Note: This function is first called on
        # the furthest-down element of the array.
        # This is because the array is sorted continually,
        # and things are only pushed and pulled from the ends
        # of the array, with heapishness guaranteed each step.
        if the_current_branch_index != 1:
            index_of_the_parent_branch = the_current_branch_index / 2
            if self.the_maxheap_array[index_of_the_parent_branch] \
               < self.the_maxheap_array[the_current_branch_index]:

                self.the_maxheap_array[the_current_branch_index], \
                    self.the_maxheap_array[index_of_the_parent_branch] \
                    = self.the_maxheap_array[index_of_the_parent_branch], \
                    self.the_maxheap_array[the_current_branch_index]
            # If the current conditional is in effect, we must be
            # suspicious of the heapity of the rest of the tree above it.
            # To do this in a while loop, simply swap the index we're
            # currently examining with that of the parent.
            self._up_propagate_heap_property(index_of_the_parent_branch)





    def pop(self):
        ''' Return a value from the root of the heap,
        maintaining the heap properpty. '''
        if len(self.the_maxheap_array) <= 1:
            raise ValueError("Attempted to pop() from an empty array.")
            return
        else:
            # Save the root to return ...
            value_to_return = self.the_maxheap_array[1]
            # ... overwrite the head with a copy of the tail ...
            self.the_maxheap_array[1] = \
                self.the_maxheap_array[(len(self.the_maxheap_array) - 1)]
            # ... and chop off the original tail.
            del self.the_maxheap_array[(len(self.the_maxheap_array) - 1)]
        # This is likely to deheaperize the array, so down-propagate the
        # heap property from the root of the heap.
        self._down_propagate_heap_property(1)
        return value_to_return
    '''
    def _down_propagate_heap_property(self):
        # Deprecated, recursive is better.
        the_current_branch_index = self.the_maxheap_array[1]
        while the_current_branch_index < len(self.the_maxheap_array):
            the_left_branch_index = 2 * the_current_branch_index
            the_right_branch_index = 2 * the_current_branch_index + 1
            if self.the_current_branch_index < len(self.the_maxheap_array) - 2:
                # the -2 is where I realized while was not a good idea;
                # this function is incomplete as a result.

                # Check for heap property compliance with
                # the node to the right, and then the node to the left.
                if self.the_maxheap_array[the_current_branch_index] \
                   < self.the_maxheap_array[the_right_branch_index]:

                    # If they are insufficiently heapy, swap them.
                    self.the_maxheap_array[the_current_branch_index], \
                        self.the_maxheap_array[the_right_branch_index] \
                        = self.the_maxheap_array[the_right_branch_index], \
                        self.the_maxheap_array[the_current_branch_index]
                    # If the above occurs, you don't need to check
                    # the left branch because the thing you swapped upwards
                    # (the right branch) is guaranteed to be bigger
                    # than the left branch due to previous enheapifications.
                    the_branch_index_for_the_next_pass = \
                        the_right_branch_index
                # Repeat this procedure for the other branch, if necessary.
                elif self.the_maxheap_array[the_current_branch_index] \
                   < self.the_maxheap_array[the_left_branch_index]:

                    self.the_maxheap_array[the_current_branch_index], \
                        self.the_maxheap_array[the_left_branch_index] \
                        = self.the_maxheap_array[the_left_branch_index], \
                        self.the_maxheap_array[the_current_branch_index]
                    the_branch_index_for_the_next_pass = \
                        the_left_branch_index
    '''

    def _compare_adjacent_nodes(self, left, right):

    '''
    # This also didn't work.
    # The whole thing needs to be refactored to separate functions.
    def _down_propagate_heap_property(self, the_current_branch_index):
        # The recursive solution.
        # I first did this as a while loop, but it seemed to be even longer.
        # This looked awful when I took out the extra lines,
        # so I decided to leave them in.

        # The following is also for readability:
        the_array = self.the_maxheap_array

        if the_current_branch_index < len(the_array):

            left_index = 2 * the_current_branch_index
            right_index = 2 * the_current_branch_index + 1

            if right_index < len(the_array):

                if the_array[the_current_branch_index] \
                   < the_array[right_index]:

                    # If they are insufficiently heapy, swap them.
                    the_array[the_current_branch_index], \
                        the_array[right_index] \
                        = the_array[right_index], \
                        the_array[the_current_branch_index]

                    self._down_propagate_heap_property(right_index)

                    # To prevent unnecessary left-branch checking:
                    conducted_an_operation_on_the_right_branch = True

            if left_index < len(the_array) \
               and conducted_an_operation_on_the_right_branch is not True:

                if the_array[the_current_branch_index] \
                   < the_array[left_index]:

                    the_array[the_current_branch_index], \
                        the_array[left_index] \
                        = the_array[left_index], \
                        the_array[the_current_branch_index]

                    self._down_propagate_heap_property(left_index)
    '''
