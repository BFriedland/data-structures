
# A priority queue's properties can be precisely modeled by a binary heap.
# Therefore, this priority queue copies my binary heap data structure closely.

# References used:
# http://domenicosolazzo.wordpress.com/2010/09/26/heapsort-a-python-example/
# http://pravin.paratey.com/posts/binary-heaps-and-priority-queues
# And, most of all:
# https://github.com/jbbrokaw/data-structures/blob/master/binheap.py


class Node:

    def __init__(self, value, priority):

        if not value:
            raise ValueError("Nodes must have a value to be inserted into the priority queue.\nSyntax: Node(value, priority)")
        else:
            self.value = value
        if not priority:
            raise ValueError("Nodes must have a priority to be inserted into the priority queue.\nSyntax: Node(value, priority)")
        else:
            self.priority = priority


class PriorityQueue():
    ''' Create a priority queue with insert(item) and pop() functions,
    optionally taking a supplied_iterable keyword parameter. '''

    def __init__(self, supplied_iterable=None):

        self.the_array = [[None]]

        if supplied_iterable is not None:
            # Preempt non-iterable input with an exception
            try:
                for each_thing in supplied_iterable:
                    self.insert(each_thing)
            except:
                raise Exception("supplied_iterable must be an iterable")

    def _highest_index(self):
        # For readability later on.
        return (len(self.the_array) - 1)

    def insert(self, item):
        ''' Insert a new item into the bottom of the priority queue,
        maintaining the order of priority. '''

        if not isinstance(item, Node):
            raise ValueError("Only Nodes may be inserted into the priority queue.")

        self.the_array.append(item)
        self._up_propagate_priority_order()

    def _up_propagate_priority_order(self):

        # It always up-propagates from the bottom.
        current_index = len(self.the_array) - 1

        parent_index = current_index // 2

        # Prevent index bound errors and only check
        # the immediately following nodes:
        while ((current_index > 1)
               and (self.the_array[current_index].priority
               > self.the_array[parent_index].priority)):

            # Swapping both items at once:
            self.the_array[current_index], self.the_array[parent_index] \
                = self.the_array[parent_index], self.the_array[current_index]

            # Moving up the tree:
            current_index = parent_index
            parent_index = current_index // 2

    def peek(self):
        ''' Return the most important item
        without removing it from the queue. '''

        if len(self.the_array) > 1:

            return self.the_array[1]

        else:

            raise ValueError("Cannot peek at empty queue")

    def pop(self):

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

    def _largest_valid_branch(self, current_index):

        # Important: This compares indices everywhere EXCEPT on the
        # next to last condition, where .priority is compared.

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
        # Otherwise, compare their items and return the greater one:
        if self.the_array[left_branch].priority \
           > self.the_array[right_branch].priority:
            return left_branch
        else:
            return right_branch

    def _down_propagate_priority_order(self):

        # Always begin at the top when down-propagating.
        current_index = 1

        the_index_to_swap_from = self._largest_valid_branch(current_index)

        while ((the_index_to_swap_from <= self._highest_index())
               and (self.the_array[the_index_to_swap_from].priority
                    > self.the_array[current_index].priority)):

            # Swapswapswap
            self.the_array[current_index],
            self.the_array[the_index_to_swap_from]         \
                = self.the_array[the_index_to_swap_from],  \
                self.the_array[current_index]

            # These variables need to be refreshed every pass.
            current_index = the_index_to_swap_from
            the_index_to_swap_from = self._largest_valid_branch(current_index)

