
# the heapq docs contain notes about how to make a priority queue with heapq
# Queue.PriorityQueue also has stuff.
#   timeout is only because of multiprocessing,
#       no need to care about that for this
# it's not push() and pop(),
# it's put() and get()
# Queue.Queue is best sez DTH, cause of simplification
# priorityqueue needs tuples (priority, value)
# it is sorted in min priority order: 1, 2, 3, 4...

from Queue import Queue




class Node:

    def __init__(self, value):

        self.value = value
        self.edges_for_this_node = []


class Edge:

    def __init__(self, alpha_node, beta_node):

        self.alpha_node = alpha_node
        self.beta_node = beta_node


class TraversableGraph:

    def __init__(self):

        self.node_list = []
        self.edge_list = []

    def nodes(self):
        ''' Return a list containing all Nodes in the TraversableGraph. '''

        node_list_to_return = []
        for each_node in self.node_list:
            node_list_to_return.append(each_node.value)
        return node_list_to_return

    def edges(self):
        ''' Return a list containing the Node values
        of every Edge in the TraversableGraph contained in separate
        tuples within the returned list.. '''

        edge_list_to_return = []
        for each_edge in self.edge_list:
            alpha_node = each_edge.alpha_node
            beta_node = each_edge.beta_node
            node_tuple = (alpha_node, beta_node)
            edge_list_to_return.append(node_tuple)

        return edge_list_to_return

    def add_node(self, n, _returning=False):
        ''' Add a new Node with the value n to the TraversableGraph. '''

        new_node = Node(n)
        self.node_list.append(new_node)

        if _returning is True:
            return new_node

    def add_edge(self, n1, n2):
        ''' Add an edge connecting the nodes n1 and n2. '''

        if self.has_node(n1) is False:
            node_one = self.add_node(n1, _returning=True)
        else:
            node_one = self._return_node_with_this_value(n1)
        if self.has_node(n2) is False:
            node_two = self.add_node(n2, _returning=True)
        else:
            node_two = self._return_node_with_this_value(n2)

        new_edge = Edge(node_one, node_two)

        node_one.edges_for_this_node.append(new_edge)
        node_two.edges_for_this_node.append(new_edge)

        self.edge_list.append(new_edge)

    def has_node(self, n):
        ''' Return True if n is contained in the graph
        and False if n is not contained in the graph. '''

        for each_node in self.node_list:
            if each_node.value == n:
                return True
        return False

    def _return_node_with_this_value(self, n):
        ''' Return the Node object with the given value n. '''

        for each_node in self.node_list:
            if each_node.value == n:
                return each_node

    def del_node(self, n):
        ''' Deletes the edge connecting the node n from the graph,
        raising an error if no such node exists; also removes all edges
        connecting to the node n. '''

        if self.has_node(n) is False:

            raise Exception("{} not in TraversableGraph".formate(n))

        for each_edge in self.edge_list:

            # This design decision means Nodes with identical values
            # are considered to be identical nodes.
            if n == each_edge.alpha_node or n == each_edge.beta_node:

                self.edge_list.remove(each_edge)

        for each_node in self.node_list:

            if n == each_node.value:

                # del did not work here.
                # I think it was removing the reference
                # and NOT removing the thing from the list.
                # Fortunately, since objects with no external
                # references are garbage-collected automatically
                # by Python during execution, removing it from
                # all the lists should be sufficient.
                # But oerhaps not, since it might still bounce
                # references around with its own Edges, which were
                # also remove()d... hmm! A question for another day.
                self.node_list.remove(each_node)

    def del_edge(self, n1, n2):
        ''' Delete the Edge connecting the Nodes with values n1 and n2
        from the TraversableGraph. Raise an exception if no such Edge exists. '''

        found_the_correct_edge = False
        for each_edge in self.edge_list:
            alpha_node_value = each_edge.alpha_node.value
            beta_node_value = each_edge.beta_node.value
            if (n1 == alpha_node_value) or (n1 == beta_node_value):
                # This used to be AND, but a second conditional is clearer:
                if (n2 == alpha_node_value) or (n2 == beta_node_value):
                    self.edge_list.remove(each_edge)
                    # Take this Edge out of its Nodes:
                    each_edge.alpha_node.edges_for_this_node.remove(each_edge)
                    each_edge.beta_node.edges_for_this_node.remove(each_edge)
                    # Tell Python it doesn't have to freak out:
                    found_the_correct_edge = True
        if found_the_correct_edge is False:
            raise Exception("Edge ({}, {}) not in TraversableGraph".format(n1, n2))

    def neighbors(self, n):
        ''' Return the list of all Nodes connected to Node n by Edges.
        Raise an exception if n is not in the TraversableGraph. '''

        if self.has_node(n) is False:
            raise Exception("{} not in TraversableGraph.\nTraversableGraphlist: {}".format(n.value,
                            self.nodes()))

        list_of_nodes_connected_to_n = []

        # Append the neighbors' values but not the supplied value:
        for each_edge in self.edge_list:

            if ((each_edge.alpha_node.value != n)
               and (each_edge.beta_node.value == n)):

                list_of_nodes_connected_to_n.append(each_edge.alpha_node.value)

            # Elif prevents multiple inclusion for Nodes with duplicate values:
            elif ((each_edge.alpha_node.value == n)
               and (each_edge.beta_node.value != n)):

                list_of_nodes_connected_to_n.append(each_edge.beta_node.value)

        return list_of_nodes_connected_to_n

    def adjacent(self, n1, n2):
        ''' Return True if Nodes with values n1 and n2
        are connected by an Edge and False if they are not.
        Raises an error if either of the supplied
        Nodes are not in the TraversableGraph. '''

        if not self.has_node(n1):
            raise Exception("{} not in TraversableGraph".format(n1))

        if not self.has_node(n2):
            raise Exception("{} not in TraversableGraph".format(n2))

        for each_edge in self.edge_list:
            # Spread out and euonymized to make it easier to read:
            alpha_node_value = each_edge.alpha_node.value
            beta_node_value = each_edge.beta_node.value
            if (n1 == alpha_node_value) or (n1 == beta_node_value):
                if (n2 == alpha_node_value) or n2 == (beta_node_value):
                    return True
        return False

    def _return_edge_between_these_nodes(self, n1, n2):

        primary_node = self._return_node_with_this_value(n1)
        for each_edge in primary_node.edges_for_this_node:
            alpha_node_value = each_edge.alpha_node.value
            beta_node_value = each_edge.beta_node.value
            if alpha_node_value == n2 or beta_node_value == n2:
                return each_edge
        raise Exception("Internal structure error: failed Edge Node indexing")

    # g.depth_first_traversal(start):
    #     Perform a full depth-first traversal of the graph beginning at start.
    #     Return the full visited path when traversal is complete.
    def depth_first_traversal(self, start):

        # Well-informed (possibly to the point of nearly copying) by:
        # http://eddmann.com/posts/
        #    depth-first-search-and-breadth-first-search-in-python/

        # Seed the stack with where ever we're starting.
        stack_to_visit = [self._return_node_with_this_value(start)]
        # The visited nodes list will serve as a record of our path.
        previously_visited_nodes = []
        ## DEBUGGING
        previous_values = []
        ## / DEBUGGING

        # To demonstrate that the order of lists is constant:
        crossed_edges = []

        # Due to mid-loop population of the graph, this will
        # continue until the end of the graph has been reached:
        # ... this was wrong
        # It allows things unconnected to the graph to make the thing break
        # This is because unconnected nodes still in the graph increase
        # the size of len(self.node_list), but are not appended to the stack.
        # To fix this, base the while loop on the size of the stack.
        # while len(previously_visited_nodes) < len(self.node_list):
        while len(stack_to_visit) > 0:


            current_node = stack_to_visit.pop()

            ## DEBUGGING
            print("\ncurrent_node neighbors:\n" + str(self.neighbors(current_node.value)))
            list_of_values_in_stack_to_visit = [each.value for each in stack_to_visit]
            print("\nstack_to_visit:\n" + str(list_of_values_in_stack_to_visit))
            ## / DEBUGGING

            # Must come before stack_to_visit.append(each_neighbor), below.
            # Prevents duplication of the last Node in the list.
            previously_visited_nodes.append(current_node)

            for each_value in self.neighbors(current_node.value):
                # This is inefficient but economizes on writing new functions.
                # If desired, can be fixed by implementing an internal call
                # for _neighbor_nodes() (that accepts a Node, perhaps).
                each_neighbor = self._return_node_with_this_value(each_value)

                if each_neighbor not in previously_visited_nodes:
                    stack_to_visit.append(each_neighbor)

            # Building the crossed_edges.
            # If there's nothing in the list,
            # no edge has yet been crossed.
            if len(previously_visited_nodes) > 0:
                highest_index = (len(previously_visited_nodes) - 1)
                last_visited_node = previously_visited_nodes[highest_index]
                # This is inefficient but economizes on writing new functions.
                # If desired, can be fixed by renaming the method
                # _return_edge_between_these_nodes() to
                # _return_edge_between_the_nodes_with_these_values()
                # and making a new method named
                # _return_edge_between_these_nodes() that actually does
                # what it's supposed to do in the name, now that we've
                # ensured there's a meaningful difference.
                # ...
                # DUPLICATE EDGES NOTE!
                # This will seem to make duplicate edges when
                # the algorithm heads back to a previous branching point.
                # This is because when the stack drops off a cliff,
                # crossed_edge DOES NOT CHANGE from the value it was
                # the previous pass.
                # This CANNOT BE AVOIDED with this particular approach,
                # you'd have to write a little check for if
                # self._return_edge_between_these_nodes() does not return
                # anything (it fails silently?) (it should return an
                # exception on the line where it says
                # "Internal structure error: failed Edge Node indexing")
                # Fortunately the edges don't seem to matter. Currently.
                # Or that seemed to be how it works. I don't really know yet...
                crossed_edge = self._return_edge_between_these_nodes(
                    current_node.value,
                    last_visited_node.value)
                crossed_edges.append(crossed_edge)

            ## DEBUGGING
            previous_values.append(current_node.value)
            ## / DEBUGGING




        # It always duplicates the final step once and it's getting too
        # late for me to figure out why.
        previously_visited_nodes.pop()
        crossed_edges.pop()



        # Presumably this maintains sorting order...
        # ... I decided to demonstrate this by creating a parallel list
        # full of the Edges that have been visited as well, in order.
        previously_visited_node_values \
            = [each_node.value for each_node in previously_visited_nodes]


        previously_visited_edge_values \
            = [(each_edge.alpha_node.value, each_edge.beta_node.value)
               for each_edge in crossed_edges]



        return previously_visited_node_values, previously_visited_edge_values



    # circular_graph = traversable_graph.TraversableGraph()
    # for each_integer in range(0, 10):
    #     circular_graph.add_node(each_integer)
    # # range(0, 10) gives 0 though 9 and len(that) gives 10
    # for each_index in range(1, len(circular_graph.node_list)):
    #     circular_graph.add_edge((each_index - 1), each_index)
    # # Tie the graph chain together at the ends:
    # circular_graph.add_edge(0, (len(circular_graph.node_list)-1))  # should be .value


    # circular_graph.add_node("alpha")
    # circular_graph.add_node("omega")
    # circular_graph.add_edge("alpha", 4)
    # circular_graph.add_edge("omega", "alpha")

    # circular_graph.add_node("hello")
    # circular_graph.add_node("kitty")
    # circular_graph.add_node("aren't")
    # circular_graph.add_node("you")
    # circular_graph.add_node("adorable")
    # circular_graph.add_edge("hello", "alpha")
    # circular_graph.add_edge("kitty", "adorable")
    # circular_graph.add_edge("aren't", 6)
    # circular_graph.add_edge("you", "alpha")
    # circular_graph.add_edge("adorable", "you")
    # #import pdb
    # #pdb.set_trace()
    # circular_graph.depth_first_traversal("alpha")

    # Example results:
    # ['alpha',
    #   'you',
    #   'adorable', <-- step before it; see the edge prints pattern of each thing always being first in at least one edge, except on the jumped one, which is duplicated second (first=left, second=right)
    #   'kitty', <--jump
    #   'hello', <--land
    #   'omega',
    #   4,
    #   5,
    #   6,
    #   "aren't",
    #   7,
    #   8,
    #   9,
    #   0,
    #   1, <--jump??
    #   2, <--land??
    #   3]

    # g.breadth_first_traversal(start):
    #     Perform a full breadth-first traversal of the graph, beginning at start.
    #     Return the full visited path when traversal is complete.

    def breadth_first_traversal(self, start):






















# In addition, write some demonstration code in
# an "if __name__ == '__main__':" block at the end of your file
# that shows how the two methods of traversal compare to each other
# when performed on the same graph.
# See if you can demonstrate the performance characteristics
# of the two methods over a variety of graph orders.
