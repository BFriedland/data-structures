'''

Contains a Queue class for constructing queues out of Node objects.

This queue implementation copies heavily from test_linked_list
in my data-structures repository.

Partly adapted from:
http://en.literateprograms.org/Singly_linked_list_%28Python%29
'''


class Queue:

    def __init__(self):

        self.head = None
        self.tail = None

        self.number_of_created_nodes = 0
        self.number_of_deleted_nodes = 0

        self.previously_placed_node = None

    def enqueue(self, supplied_data):

        ''' Insert a new node with supplied_data at the head of the queue. '''

        new_node = Node()

        new_node.data = supplied_data

        new_node.next_node = self.head
        print("new_node.next_node == %r" % (self.head))

        if self.head is not None:
            self.head.previous_node = new_node
            print("self.head == %r" % (new_node.data))

        if self.tail is None:
            self.tail = new_node
            print("self.tail == %r" % (new_node))

        self.head = new_node
        print("self.head == %r" % (new_node.data))

        # Temporary self-reference; doing this makes dequeue remove
        # the correct objects.
        # My suggestion is writing it all out with boxes and arrows
        # and numbers on a piece of paper. Much easier to understand that way.
        new_node.previous_node = new_node
        print("new_node.previous_node == %r" % (new_node.data))

        self.number_of_created_nodes += 1


    def dequeue(self):

        ''' Remove the value off the tail of the queue and return it. '''

        # This method was much more complicated to implement and debug
        # than I anticipated. There's almost certainly a simpler way,
        # but this is functional and perhaps efficient enough,
        # so I'm keeping it for now.

        if self.tail is None:

            raise Exception

        else:

            try:

                value_to_return = self.tail.data
                print("value_to_return == %r" % (value_to_return))

                # This moves the tail forward and discards
                # the dequeued Node's references.
                # This is checking whether the tail is really the trailing Node
                # AND
                # whether the tail is not the only Node in the list
                # (by being self.head too)
                if (self.tail.next_node is None) and (self.tail != self.head):

                    # self.tail.previous_node = None # should be
                    # self.tail = None, since the conditional checks
                    # if the node we moved one dequeue() ago is None
                    # (thus, this dequeue() we nust be removing
                    # the current node, self.tail).
                    self.tail = self.tail.previous_node
                    print("self.tail. == %r" % (self.tail))

                    # Don't remove this line just because of the conditional!
                    # This is changing self.tail.next_node after
                    # self.tail itself has already been changed.
                    # Sleepy is bad.
                    self.tail.next_node = None

                elif self.tail == self.head:
                    # If they're both the last or first queue object,
                    # they should both be wiped after their data is returned.
                    self.tail = None
                    self.head = None

                elif self.tail.next_node is not None:
                    # The tail Node's next_node should always be None.
                    # Since we already moved the tail forward outside of
                    # this conditional, clean up the next_node reference here:
                    self.tail.next_node = None
                    print("self.tail.next_node == %r" % (self.tail.next_node))
                    # This step shouldn't strictly be necessary, but for
                    # ease of debugging make it explicit for now.

                if value_to_return is not None:

                    self.number_of_deleted_nodes += 1

                return value_to_return

            except:

                raise Exception

    def size(self):

        size_of_the_queue = self.number_of_created_nodes - self.number_of_deleted_nodes

        return size_of_the_queue


class Node:

    def __init__(self):

        self.data = None
        self.next_node = None
        self.previous_node = None







