'''

Contains a Stack class for constructing stacks out of Node objects.

This stack implementation copies heavily from test_linked_stack
in my data-structures repository.

Partly adapted from:
http://en.literateprograms.org/Singly_linked_stack_%28Python%29
'''


class Stack:

    def __init__(self):

        self.head = None

    def push(self, data):

        ''' Insert a new node with given data at the head of the stack. '''

        # The specifications explicitly said "at the head of the stack",
        # so this function will have no way to push at arbitrary indices.

        new_node = Node()

        new_node.data = data

        new_node.next_node = self.head

        self.head = new_node

    def pop(self):

        ''' Remove the value off the head of the stack and return it. '''

        # For some reason I got the following error here when I tried
        # to use try:except for this:
        #
        # Traceback (most recent call last):
        #    File "test_stack.py", line 84, in test_pop
        #        self.assertRaises(Exception,
        #                          self.test_stack_for_no_nodes.pop())
        #    File "/Users/fried/Desktop/CodeFellows/repos/data-structures/stack
        # /stack.py", line 55, in pop
        #        raise Exception
        # Exception
        #
        # I don't know why this failed assertRaises(Exception, ...) when
        # it clearly raised Exception.
        # ...
        # Teh Googs say this is because in this case assertRaises needs
        # to be used as a context manager in unit testing.

        if self.head is None:

            raise Exception

        else:

            value_to_return = self.head.data

            # This is simply moving the next_node redirect forward.
            # Deletes nothing but the reference.
            self.head = self.head.next_node

            # Note that "None" is the redirect value for the very first Node.
            # The stack will self-maintain its start this way.
            # A more thorough implementation would include a dummy node
            # with special functions to make every Stack function bounce off
            # the floor instead of sending errors due to the use of None.

            return value_to_return


class Node:

    def __init__(self):

        self.data = None
        self.next_node = None
