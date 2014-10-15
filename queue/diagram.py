   def enqueue(self, data):

        ''' Insert a new node with given data at the head of the queue. '''

        new_node = Node()

        new_node.data = data

        new_node.next_node = self.head

        if self.head is not None:

            self.head.previous_node = new_node

        if self.tail is None:

            self.tail = new_node

        self.head = new_node

        new_node.previous_node = new_node

Step 0

head
tail
None


Step 1

      head
      tail
None     1
      nx:N
      pv:1


Step 2

            head
      tail
None     1     2
      nx:N  nx:1
      pv:2  pv:2


Step 3

                  head
      tail
None     1     2     3
      nx:N  nx:1  nx:2
      pv:2  pv:3  pv:3



    def dequeue(self):

        ''' Remove the value off the tail of the queue and return it. '''

        if self.tail is None:

            raise Exception

        else:

            value_to_return = self.tail.data

            self.tail = self.tail.previous_node

            if self.tail.next_node is not None:

                self.tail.next_node.previous_node = None

            # else: # make it explicit instead:
            elif self.tail.next_node is None:

                # self.tail.previous_node = None # should be self.tail = None, since the conditional checks if the node we moved one dequeue() ago is None (thus, this dequeue() we nust be removing the current node, self.tail).
                self.tail = None

            self.tail.next_node = None

            self.deleted_nodes += 1


Step 4

               head
          tail
None    1    2    3
     nx:N nx:N nx:2
     pv:N pv:3 pv:3


Step 5


               tail
None    1    2    3
               nx:N # beep beep error found
          pv:N



















