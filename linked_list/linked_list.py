'''

Contains a LinkedList class for constructing linked lists out of Node objects.

Partly adapted from:
http://en.literateprograms.org/Singly_linked_list_%28Python%29
'''


class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

        self.number_of_created_nodes = 0
        self.number_of_deleted_nodes = 0

    def insert(self, val):

        ''' Insert a new node with given data at the head of the list. '''

        # The specifications explicitly said "at the head of the list",
        # so this function will have no way to insert at arbitrary indices.

        new_node = Node()

        new_node.data = val

        new_node.next_node = self.head

        if self.head is None:

            self.tail = new_node

        self.head = new_node

        self.number_of_created_nodes += 1

    def pop(self):

        ''' Remove the value off the head of the list and return it. '''

        value_to_return = self.head.data

        # This is simply moving the next_node redirect forward.
        # Deletes nothing but the reference.
        self.head = self.head.next_node

        # Note that "None" is the redirect value for the very first Node.
        # The list will self-maintain its start this way.
        # A more thorough implementation would include a dummy node
        # with special functions to make every LinkedList function bounce off
        # the floor instead of sending errors due to the use of None.

        # If the node being removed is the final node,
        # remember to set self.tail to None.
        # This behavior will default to making the tail equal to
        # the head if the snake is decapitated. This will more readily
        # reveal any possible future errors relating to removing
        # the head when you're not supposed to.
        if self.head is None:
            self.tail = None

        self.number_of_deleted_nodes += 1

        return value_to_return

    def size(self):

        ''' Return length of the list. '''

        return (self.number_of_created_nodes - self.number_of_deleted_nodes)

    def search(self, val):

        ''' Traverse the list and return the node containing
        the supplied value if present; otherwise, return None. '''

        if self.head is None:
            return None

        else:
            return self.head.search_self_or_next_node_for_a_value(val)

    def remove(self, node):

        ''' Remove a given Node from the list, where ever it might be. '''

        # This operation is unusually complex due to the number of
        # things that need to be kept track of. The head and the tail are both
        # special cases, each with their own re-tagging considerations.

        # If the list has no nodes, it's still possible for a node
        # reference to continue existing.
        # To preempt this, return None if the list is headless.
        if self.head is None:

            return None

        else:

            # The head always has None for a previous node.
            node_before_the_node_to_remove, node_to_remove = \
                self.head.search_self_or_next_node_for_identity_match(None, node)

            # If the node being removed is neither the head nor the tail,
            # it needs to bridge the gap in order to be
            # "removed" from the list.
            if (node_to_remove != self.tail) and (node_to_remove != self.head):

                node_after_the_node_to_remove = node_to_remove.next_node

                # This bridges the list, effectively
                # removing the node_to_remove.
                node_before_the_node_to_remove.next_node = \
                    node_after_the_node_to_remove

            if node_to_remove == self.tail:

                # This sort of operation always feels wrong to type
                # since it isn't removing anything but the reference,
                # but that's how this LinkedList works.
                # It deletes nothing, only swapping references.
                if node_before_the_node_to_remove is not None:
                    node_before_the_node_to_remove.next_node = None

                self.tail = node_before_the_node_to_remove

            if node_to_remove == self.head:

                self.head = node_to_remove.next_node

        self.number_of_deleted_nodes += 1

    def __str__(self):
        # pass

        # def print_list(self):

        ''' Print the entirety of the list
        represented as a Python tuple literal. '''

        if self.head is None:

            string_to_return = "()"

        else:

            node_to_check = self.head

            incrementor_for_node_printing = 0

            string_to_return = "("

            while True:

                # If there's only one thing in the list, it doesn't need
                # the leading comma.
                # Or if the thing we're about to add is the first thing.
                if incrementor_for_node_printing != 0:

                    string_to_return += ", "

                if isinstance(node_to_check.data, str):

                    # If it's a string, make it pretend to be a string. o_o
                    string_to_return += "'" + str(node_to_check.data) + "'"

                else:

                    string_to_return += str(node_to_check.data)

                incrementor_for_node_printing += 1

                # Terminate assembling the string at the tail of the list.
                if node_to_check != self.tail:

                    node_to_check = node_to_check.next_node

                else:

                    break

            string_to_return += ")"

        return string_to_return


class Node:

    def __init__(self):

        self.data = None
        self.next_node = None

    def search_self_or_next_node_for_a_value(self, value):

        # This method is the recursive part of LinkedList.search()

        if self.data == value:
            return self

        elif self.next_node is None:
            return None

        else:
            return self.next_node.search_self_or_next_node_for_a_value(value)

    def search_self_or_next_node_for_identity_match(self, previous_node,
                                               supplied_node):

        # This method is the recursive part of LinkedList.remove()

        if self == supplied_node:
            return previous_node, self

        # Leaving this in because it's possible a node reference will remain
        # even after it has had its ties deleted.
        elif self.next_node is None:
            return previous_node, None

        else:
            # This should return the previous_node identity
            # for the last call.
            # It drags up the returned elements from the very bottom.
            return self.next_node \
                       .search_self_or_next_node_for_identity_match(
                           self, supplied_node)
