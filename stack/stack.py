'''
Contains a Stack class for constructing stacks out of Node objects.

This stack implementation copies heavily from test_linked_list
in my data-structures repository.

Partly adapted from:
http://en.literateprograms.org/Singly_linked_list_%28Python%29
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
