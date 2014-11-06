
# A priority queue's properties can be precisely modeled by a binary heap.
# Therefore, this priority queue copies my binary heap data structure closely.

# References used:
# http://domenicosolazzo.wordpress.com/2010/09/26/heapsort-a-python-example/
# http://pravin.paratey.com/posts/binary-heaps-and-priority-queues
# And, most of all:
# https://github.com/jbbrokaw/data-structures/blob/master/binheap.py

# Significantly refurbished with help from:
# http://interactivepython.org/runestone/static/pythonds/Trees/heap.html


class Node:

    def __init__(self, value, priority):

        if not value:
            raise ValueError("Nodes must have a value to be inserted"
                             " into the priority queue."
                             "\nSyntax: Node(value, priority)")
        else:
            self.value = value
        if not priority:
            raise ValueError("Nodes must have a priority to be inserted"
                             " into the priority queue."
                             "\nSyntax: Node(value, priority)")
        else:
            self.priority = priority


class PriorityQueue:
    ''' Create a priority queue with insert(item) and pop() functions,
    optionally taking a supplied_iterable keyword parameter. '''

    def __init__(self, max_or_min="min", supplied_iterable=None):

        self.the_array = [[None]]

        self.max_or_min = max_or_min

        if supplied_iterable is not None:
            # Preempt non-iterable input with an exception
            try:
                for each_thing, each_priority in supplied_iterable:
                    self.insert(each_thing, each_priority)
            except:
                raise Exception("supplied_iterable must be an iterable;"
                                " was type {}".format(type(supplied_iterable)))

    def _highest_index(self):
        # For readability later on.
        #return (len(self.the_array) - 1)
        return len(self.the_array)

    def insert(self, item, priority):
        ''' Insert a new item into the bottom of the priority queue,
        maintaining the order of priority. '''

        node_to_insert = Node(item, priority)
        self.the_array.append(node_to_insert)
        self._up_propagate_priority_order()

    def _up_propagate_priority_order(self):

        # This section refurbished with help from:
        # http://interactivepython.org/
        #                   runestone/static/pythonds/Trees/heap.html

        # It always up-propagates from the very bottom.
        current_index = len(self.the_array) - 1
        parent_index = current_index // 2

        current_node = self.the_array[current_index]
        parent_node = self.the_array[parent_index]

        # Prevent index bound errors:
        while parent_index > 0:

            # In a heap, this comparison determines max vs min heapness.
            # In a priority queue it is the same.
            # > for max, < for min.
            if self.max_or_min == "max":
                if current_node.priority > parent_node.priority:
                    # Swap:
                    parent_node, current_node = current_node, parent_node
                else:
                    # Moving up the tree:
                    current_index = parent_index
                    parent_index = current_index // 2
            else:
                if current_node.priority < parent_node.priority:
                    # Swap:
                    parent_node, current_node = current_node, parent_node
                else:
                    # Moving up the tree:
                    current_index = parent_index
                    parent_index = current_index // 2

    def peek(self):
        ''' Return the most prioritized item
        from the priority queue, maintaining order. '''

        if len(self.the_array) > 1:
            return self.the_array[1]
        else:
            raise ValueError("Cannot peek at empty queue")

    def pop(self):
        ''' Remove and return the most prioritized item
        from the priority queue, maintaining order. '''
        item_to_return = self.the_array[1]

        if len(self.the_array) > 2:
            # ... reminded of the standard functions by jbbrokaw...
            self.the_array[1] = self.the_array.pop()

        elif len(self.the_array) == 2:
            self.the_array.pop()
            # Since there is no more array, the function has to end.
            # Or else.
            return item_to_return

        # Don't disturb the None.
        else:
            raise IndexError

        # Now ensure it is in fact in order of priority.
        self._down_propagate_priority_order()

        return item_to_return

    def _min_or_max_subbranch(self, current_index):
        ''' Return the child branch with the greatest or least priority,
        depending on heap type/priority order type, no matter which
        it may be. Used when down-propagating the appropriate property. '''

        left_branch_index = (2 * current_index)
        right_branch_index = ((2 * current_index) + 1)
        highest_branch_index = self._highest_index()

        # If the derived value of the greater branch's index
        # has a higher index than that of the highest branch index,
        # return the left branch.
        # This conditional is sufficient since _min_or_max_subbranch() is
        # only ever called inside a while loop with an execution condition
        # that specifies (2 * current_index) <= self._highest_index().
        if right_branch_index > highest_branch_index:
            return left_branch_index

        elif self.max_or_min == "min":
            # If the left branch's priority is smaller than the right
            # branch's priority, return the left branch.
            if (self.the_array[left_branch_index].priority
               < self.the_array[right_branch_index].priority):
                return left_branch_index

            else:
                return right_branch_index

        else:
            # If the left branch's priority is greater than the right
            # branch's priority, return the left branch.
            if (self.the_array[left_branch_index].priority
               > self.the_array[right_branch_index].priority):
                return left_branch_index

            else:
                return right_branch_index

    def _down_propagate_priority_order(self):

        # This section refurbished with help from:
        # http://interactivepython.org/
        #                   runestone/static/pythonds/Trees/heap.html

        if len(self.the_array) <= 2:
            # Then there's only [None], or [None] and the Node;
            # thus, either [None] or the Node is already highest priority.
            return

        # Always begin at the top when down-propagating.
        current_index = len(self.the_array) - 1
        current_node = self.the_array[current_index]

        # Bound limiting conditional.
        # If this is False, then we are necessarily at the end.
        while (current_index * 2) <= self._highest_index():

            the_index_to_swap_from = self._min_or_max_subbranch(current_index)
            the_node_to_swap_from = self.the_array[the_index_to_swap_from]

            if self.max_or_min == "min":
                if current_index.priority < the_node_to_swap_from.priority:
                    # Swappity swapswapswap:
                    current_node, the_node_to_swap_from       \
                        = the_node_to_swap_from, current_node

            # Moving down the tree, index by index:
            current_index = the_index_to_swap_from
