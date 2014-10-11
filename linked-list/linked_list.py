'''
Partly adapted from:
http://en.literateprograms.org/Singly_linked_list_%28Python%29
'''


class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

        self.created_nodes = 0
        self.deleted_nodes = 0

    def insert(self, val):

        ''' Insert a new node with given data at the head of the list. '''

        # The specifications explicitly said "at the head of the list",
        # so this function will have no way to insert at arbitrary indices.

        new_node = Node()

        new_node.data = val

        new_node.next_node = self.head

        self.head = new_node

        if self.tail == None:

            self.tail = new_node

        self.created_nodes += 1

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

        # Make sure tail isn't pointing to a "removed" node:
        if self.head == None:
            self.tail = None

        self.deleted_nodes += 1

        return value_to_return

    def size(self):

        ''' Return length of the list. '''

        return (self.created_nodes - self.deleted_nodes)

    def search(self, val):

        ''' Traverse the list and return the node containing
        the supplied value if present; otherwise, return None. '''

        if self.head == None:
            return None

        else:
            return self.head.search_self_or_next_for_a_value(val)

    def remove(self, node):

        ''' Remove a given Node from the list, where ever it might be. '''

        # If the list has no nodes, it's still possible for a node
        # reference to continue existing.
        if self.head == None:
            return None

        else:
            # The head always has None for a previous node.
            node_before_the_node_to_remove, node_to_remove = self.head.search_self_or_next_for_identity_match(None, node)

            node_after_the_node_to_remove = node_to_remove.next_node

            # This bridges the list, effectively removing the node_to_remove.
            node_before_the_node_to_remove.next_node = node_after_the_node_to_remove

        self.deleted_nodes += 1

    def print_list(self):

        ''' Print the entirety of the list
        represented as a Python tuple literal. '''

        if self.head == None:

            print("(None)")

        else:

            node_to_check = self.head

            incrementor_for_node_printing = 0

            print("("),

            while 1:

                print("{}, '{}',".format(str(incrementor_for_node_printing), \
                                          node_to_check.data)),

                incrementor_for_node_printing += 1

                if node_to_check.next_node != None:
                    node_to_check = node_to_check.next_node

                else:

                    print(")")

                    break


class Node:

    def __init__(self):

        self.data = None
        self.next_node = None

    def search_self_or_next_for_a_value(self, value):

        # This method is the recursive part of LinkedList.search()

        if self.data == value:
            return self

        elif self.next_node == None:
            return None

        else:
            return self.next_node.search_self_or_next_for_a_value(value)

    def search_self_or_next_for_identity_match(self, \
            previous_node, supplied_node):

        # This method is the recursive part of LinkedList.remove()

        if self == supplied_node:
            return previous_node, self

        # Leaving this in because it's possible a node reference will remain
        # even after it has had its ties deleted.
        elif self.next_node == None:
            return previous_node, None

        else:
            # This should return the previous_node identity
            # for the last call.
            # It drags up the returned elements from the very bottom.
            return self.next_node.search_self_or_next_for_identity_match(self, supplied_node)

# For debugging in a REPL
test_list = LinkedList()

for each_number in range(1, 10):
    test_list.insert(each_number)
