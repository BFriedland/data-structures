'''
Contains a DoublyLinkedList class for constructing
doubly-linked lists out of Node objects.

This code borrows heavily from my linked_list.py test suite.

If comparing to linked_list, stack or queue, NOTE that
next and previous have been swapped
because it doesn't make any sense for next to point at
the head when that's also the direction you're adding things.
You don't start at the tail, you start at the head;
but if you're standing in the head and you want to move "into" the list
but you ask what the "next" node is, you'll be pointed closer to
the head instead of closer to the tail, which is confusing to me.

Informed by/partly adapted from:
http://en.literateprograms.org/Singly_linked_list_%28Python%29
'''


class Node:

    def __init__(self):

        self.data = None

        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def insert(self, val):

        the_node_to_insert = Node()

        the_node_to_insert.data = val

        # In contrast, the tail only gets updated by insert() if it is None.
        # This is the case when we are inserting the first Node,
        # and this is not the case when we are inserting any other Node.
        if self.tail is None:

            self.tail = the_node_to_insert

        # the_node_to_insert's previous_node will always be
        # self.head before it is updated.
        the_node_to_insert.previous_node = self.head

        # Now, move self.head up to the head of the list...
        self.head = the_node_to_insert

        # And, if there's a Node before the head of the list
        # (as opposed to a None), assign that previous Node's
        # next_node value to the most recently added Node,
        # which must be self.head due to the immediately preceding assignment.
        if isinstance(self.head.previous_node, Node):
            # The head always gets updated by insert().
            self.head.previous_node.next_node = self.head

    def append(self, val):

        the_node_to_append = Node()

        the_node_to_append.data = val

        if self.head is None:

            self.head = the_node_to_append

        # Remember, for append() the logic for insert() is swapped
        # in both the head/tail and next/previous places.
        the_node_to_append.next_node = self.tail

        self.tail = the_node_to_append

        # Make sure we're not trying to assign an attribute to a NoneType:
        if isinstance(self.tail.next_node, Node):
            self.tail.next_node.previous_node = self.tail

    def pop(self):

        # The inverse of shift().

        the_value_to_return = None

        # This prevents errors when pop() is called on an empty list:
        if self.head is not None:

            the_value_to_return = self.head.data

            if self.head.previous_node is not None:

                self.head.previous_node.next_node = None

                self.head = self.head.previous_node

            # In this case, the head is the final node
            # and must be deleted during pop().
            elif self.head.previous_node is None:

                self.head = None
                self.tail = None

        else:

            raise Exception('Cannot pop from empty list')

        # If self.head.next_node is None and self.head is not None,
        # that means self.head is alone during this pop(),
        # and should be removed.
        if self.head is None:

            self.tail = None

        return the_value_to_return

    def shift(self):

        # The inverse of pop().

        the_value_to_return = None

        # This prevents errors when shift() is called on an empty list:
        if self.tail is not None:

            the_value_to_return = self.tail.data

            if self.tail.next_node is not None:

                self.tail.next_node.previous_node = None

                self.tail = self.tail.next_node

            # In this case, the tail is the final node
            # and must be deleted during shift().
            elif self.tail.next_node is None:

                self.tail = None
                self.head = None

        else:

            raise Exception('Cannot shift from empty list')

        # If self.tail.previous_node is None and self.tail is not None,
        # that means self.tail is alone during this shift(),
        # and should be removed.
        if self.tail is None:

            self.head = None

        return the_value_to_return

    def remove(self, val):

        # Let's make a closure for our recursion.
        def check_the_next_node_for_this_value(the_node_we_are_examining, val):

            if the_node_we_are_examining.data == val:

                # Then the data has been found.
                # Wipe the appropriate pieces and mend the gap.

                if ((the_node_we_are_examining != self.head)
                        and (the_node_we_are_examining != self.tail)):

                    # If it's not on an end, mend the gap.

                    # Remember, these are assigning new Node links
                    # FOR the thing on the first line
                    # AWAY FROM the_node_we_are_examining and
                    # TOWARDS the thing on the second line.
                    the_node_we_are_examining.next_node.previous_node = \
                        the_node_we_are_examining.previous_node

                    the_node_we_are_examining.previous_node.next_node = \
                        the_node_we_are_examining.next_node

                # Now handle the cases when the_node_we_are_examining
                # is on one end but not both.
                # elif is necessary to prevent multiple interlink forwardings.
                elif isinstance(the_node_we_are_examining.next_node, Node):

                    self.tail = the_node_we_are_examining.next_node

                    the_node_we_are_examining.next_node.previous_node = \
                        the_node_we_are_examining.previous_node

                # elif is necessary to prevent multiple interlink forwardings.
                elif isinstance(the_node_we_are_examining.previous_node, Node):

                    self.head = the_node_we_are_examining.previous_node

                    the_node_we_are_examining.previous_node.next_node = \
                        the_node_we_are_examining.next_node

                # In this case, it's both the head and the tail.
                # Excise it.
                else:

                    self.head = None
                    self.tail = None

                # We can return this because the reference hasn't died yet,
                # even though we've already excluded it from the chain.
                return the_node_we_are_examining.data

            else:

                # Previous because we're starting at the head and moving back.
                # Again, Node type as opposed to NoneType.
                if isinstance(the_node_we_are_examining.previous_node, Node):

                    return check_the_next_node_for_this_value(
                        the_node_we_are_examining.previous_node, val)

                else:

                    return None

        # NOTE: The following conditional utilizes the closure we just defined.

        # You are not allowed to pretend that
        # an empty list can have things removed from it.
        if self.head is None:

            raise Exception('Cannot remove from empty list')

        else:

            return check_the_next_node_for_this_value(self.head, val)
