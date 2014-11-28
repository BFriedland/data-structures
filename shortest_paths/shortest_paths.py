
from Queue import Queue, PriorityQueue


class Node:

    def __init__(self, value):

        self.value = value
        self.edges_for_this_node = []


class Edge:

    def __init__(self, alpha_node, beta_node):

        self.alpha_node = alpha_node
        self.beta_node = beta_node


class ShortestPathsGraph:

    def __init__(self):

        self.node_list = []
        self.edge_list = []

    def nodes(self):
        ''' Return a list containing all Nodes in the ShortestPathsGraph. '''

        node_list_to_return = []
        for each_node in self.node_list:
            node_list_to_return.append(each_node.value)
        return node_list_to_return

    def edges(self):
        ''' Return a list containing the Node values
        of every Edge in the ShortestPathsGraph contained in separate
        tuples within the returned list.. '''

        edge_list_to_return = []
        for each_edge in self.edge_list:
            alpha_node = each_edge.alpha_node
            beta_node = each_edge.beta_node
            node_tuple = (alpha_node, beta_node)
            edge_list_to_return.append(node_tuple)

        return edge_list_to_return

    def add_node(self, n, _returning=False):
        ''' Add a new Node with the value n to the ShortestPathsGraph. '''

        # Nodes may not have duplicate values.
        if self.has_node(n):
            return

        new_node = Node(n)
        self.node_list.append(new_node)

        if _returning is True:
            return new_node

    def add_edge(self, n1, n2, _returning=False):
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

        if _returning is True:
            return new_edge

    def has_node(self, n):
        ''' Return True if n is contained in the graph
        and False if n is not contained in the graph. '''

        for each_node in self.node_list:
            if each_node.value == n:
                return True
        return False

    def del_node(self, n):
        ''' Deletes the edge connecting the node n from the graph,
        raising an error if no such node exists; also removes all edges
        connecting to the node n. '''

        if self.has_node(n) is False:

            raise Exception("{} not in ShortestPathsGraph".formate(n))

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
        ''' Delete the Edge connecting the Nodes with values
        n1 and n2 from the ShortestPathsGraph. If no such Edge
        exists, raise an exception. '''

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
            raise Exception("Edge ({}, {}) not in graph".format(n1, n2))

    def neighbors(self, n):
        ''' Return the list of all Nodes connected to Node n by Edges.
        Raise an exception if n is not in the ShortestPathsGraph. '''

        if self.has_node(n) is False:
            raise Exception("{} not in ShortestPathsGraph.\n"
                            "ShortestPathsGraphlist:\n"
                            "{}".format(n.value, self.nodes()))

        list_of_values_of_neighbors = []

        this_node = self._return_node_with_this_value(n)

        # Using the value of the Node, check this Node for Edges.
        if this_node.edges_for_this_node is None:
            return

        # Append the neighbors' values but not the supplied value:
        for each_edge in this_node.edges_for_this_node:

            if ((each_edge.alpha_node != this_node)
               and (each_edge.beta_node == this_node)):

                list_of_values_of_neighbors.append(each_edge.alpha_node.value)

            # Elif prevents multiple inclusion for Nodes with duplicate values:
            elif ((each_edge.alpha_node == this_node)
               and (each_edge.beta_node != this_node)):

                list_of_values_of_neighbors.append(each_edge.beta_node.value)

        return list_of_values_of_neighbors

    def adjacent(self, n1, n2):
        ''' Return True if Nodes with values n1 and n2
        are connected by an Edge and False if they are not.
        Raises an error if either of the supplied
        Nodes are not in the ShortestPathsGraph. '''

        if not self.has_node(n1):
            raise Exception("{} not in ShortestPathsGraph".format(n1))

        if not self.has_node(n2):
            raise Exception("{} not in ShortestPathsGraph".format(n2))

        for each_edge in self.edge_list:
            # Spread out and euonymized to make it easier to read:
            alpha_node_value = each_edge.alpha_node.value
            beta_node_value = each_edge.beta_node.value
            if (n1 == alpha_node_value) or (n1 == beta_node_value):
                if (n2 == alpha_node_value) or n2 == (beta_node_value):
                    return True
        return False

    def _return_node_with_this_value(self, n):
        ''' Return the Node object with the given value n. '''

        for each_node in self.node_list:
            if each_node.value == n:
                return each_node

    def _return_edge_between_these_nodes(self, n1, n2):
        ''' Return the Edge object between Nodes in the Graph
        with the supplied values, or Exception if any such
        Nodes or Edges cannot be found in the Graph. '''

        primary_node = self._return_node_with_this_value(n1)
        for each_edge in primary_node.edges_for_this_node:
            alpha_node_value = each_edge.alpha_node.value
            beta_node_value = each_edge.beta_node.value
            if alpha_node_value == n2 or beta_node_value == n2:
                return each_edge
        raise Exception("Internal structure error: failed Edge Node indexing")

    def depth_first_traversal(self, start):
        ''' Perform a full depth-first traversal of the graph beginning
        at start. Return the full visited path when traversal is complete. '''

        # A depth-first traversal algorithm is the same thing as
        # a breadth-first traversal algorithm, except it uses a stack
        # instead of a queue.

        # Well-informed (possibly to the point of nearly copying) by:
        # http://eddmann.com/posts/
        #    depth-first-search-and-breadth-first-search-in-python/

        starting_node = self._return_node_with_this_value(start)

        # Seed the stack with where ever we're starting.
        stack_to_visit = [starting_node]

        # The visited Nodes list will serve as a record of our path.
        previously_visited_nodes = []
        nodes_already_added_to_stack = []

        # Base the while loop on the size of the stack:
        while len(stack_to_visit) > 0:

            current_node = stack_to_visit.pop()
            previously_visited_nodes.append(current_node)

            for each_value in self.neighbors(current_node.value):
                # This is inefficient but economizes on writing new functions.
                # If desired, can be fixed by implementing an internal call
                # for _neighbor_nodes() (that accepts a Node, perhaps).
                each_neighbor = self._return_node_with_this_value(each_value)

                # This wrecks the big O value, but I don't feel like i have
                # enough time to improve it right now.
                # Probably something involving dictionaries.
                if each_neighbor not in previously_visited_nodes:
                    if each_neighbor not in nodes_already_added_to_stack:
                        stack_to_visit.append(each_neighbor)
                        nodes_already_added_to_stack.append(each_neighbor)

        previously_visited_node_values \
            = [each_node.value for each_node in previously_visited_nodes]

        return previously_visited_node_values

    def breadth_first_traversal(self, start):
        ''' Perform a full breadth-first traversal of the graph, beginning
        at start. Return the full visited path when traversal is complete. '''

        # A breadth-first traversal algorithm is the same thing as
        # a depth-first traversal algorithm, except it uses a queue
        # instead of a stack.

        # Well-informed (possibly to the point of nearly copying) by:
        # http://eddmann.com/posts/
        #    depth-first-search-and-breadth-first-search-in-python/

        # Seed the queue with where ever we're starting.
        queue_to_visit = Queue()
        queue_to_visit.put(self._return_node_with_this_value(start))
        # The visited nodes list will serve as a record of our path.
        previously_visited_nodes = []
        nodes_already_added_to_queue = []

        # Base the while loop on the size of the queue:
        while queue_to_visit.qsize() > 0:

            current_node = queue_to_visit.get()
            previously_visited_nodes.append(current_node)

            for each_value in self.neighbors(current_node.value):
                # This is inefficient but economizes on writing new functions.
                # If desired, can be fixed by implementing an internal call
                # for _neighbor_nodes() (that accepts a Node, perhaps).
                each_neighbor = self._return_node_with_this_value(each_value)

                # This wrecks the big O value, but I don't feel like i have
                # enough time to improve it right now.
                # Probably something involving dictionaries.
                if each_neighbor not in previously_visited_nodes:
                    if each_neighbor not in nodes_already_added_to_queue:
                        queue_to_visit.put(each_neighbor)
                        # Queue.Queue does not have a simply way to surveil its
                        # own contents, so we build a list to keep track of
                        # what we've added to it to prevent certain situations
                        # involving multiple neighbors:
                        nodes_already_added_to_queue.append(each_neighbor)

        previously_visited_node_values \
            = [each_node.value for each_node in previously_visited_nodes]

        return previously_visited_node_values

    def add_weighted_edge(self, n1, n2, weighting):
        ''' Add an edge connecting the nodes n1 and n2. '''

        if not (isinstance(weighting, int) or isinstance(weighting, float)):
            raise TypeError("weighting must be int or float")

        if self.has_edge(n1, n2):
            existing_edge = self._return_edge_between_these_nodes(n1, n2)
            existing_edge.weighting = weighting

        else:
            # Note: add_edge() will create node(s) if they don't exist.
            new_edge = self.add_edge(n1, n2, _returning=True)
            node_one = self._return_node_with_this_value(n1)
            node_two = self._return_node_with_this_value(n2)
            new_edge.weighting = weighting
            node_one.edges_for_this_node.append(new_edge)
            node_two.edges_for_this_node.append(new_edge)
            self.edge_list.append(new_edge)

    def return_weighting(self, n1, n2):
        ''' Return the weighting between the Nodes with
        values n1, n2; or, raise Exception if no such nodes. '''

        if (self.has_node(n1) is False) or (self.has_node(n2) is False):
            raise Exception("supplied parameters not in Graph")

        return self._return_edge_between_these_nodes(n1, n2).weighting

    def has_edge(self, n1, n2):
        ''' Return True if there is an Edge in the Graph between
        two nodes with values n1, n2; otherwise, return False. '''

        for each_edge in self.edge_list:
            alpha_node_value = each_edge.alpha_node.value
            beta_node_value = each_edge.beta_node.value
            if ((alpha_node_value == n1 or beta_node_value == n1)
               and (alpha_node_value == n2 or beta_node_value == n2)):
                return True
        return False

    def dijkstra_algorithm(self, start, end):

        # The trivial case.
        if start == end:
            return [start]

        try:
            starting_node = self._return_node_with_this_value(start)
            ending_node = self._return_node_with_this_value(end)
        except:
            raise ValueError("Cannot path between {} and {}:"
                             " no such Node(s)".format(start, end))














        # Dijkstra's algorithm is
        # hard.

        # ...

        # All the Python examples take GvR's suggestion that dictionaries
        # be used to reflect distances. In this example, all the Edges
        # in the Graph will be converted into dictionaries of dictionaries
        # to take advantage of dictionaries' efficiency.
        # This mental translation made possible by "Hyperboreus" writing at:
        # http://stackoverflow.com/
        #               questions/22897209/dijkstras-algorithm-in-python

        dictionary_of_distances = {}

        printable_dict_of_distances = {}

        for each_node in self.node_list:

            distances_for_the_edges_of_this_node = {}

            printable_dict_for_edges_of_this_node = {}

            for each_edge in each_node.edges_for_this_node:

                if each_edge.alpha_node == each_node:
                    other_node_of_this_edge = each_edge.beta_node
                elif each_edge.beta_node == each_node:
                    other_node_of_this_edge = each_edge.alpha_node

                else:
                    raise Exception("Logic error --"
                                    " Neither of this node's edge's nodes"
                                    " are this node!")

                distances_for_the_edges_of_this_node[other_node_of_this_edge] \
                    = each_edge.weighting

                printable_dict_for_edges_of_this_node[
                    other_node_of_this_edge.value] \
                    = each_edge.weighting

            dictionary_of_distances[each_node] \
                = distances_for_the_edges_of_this_node

            # Result is dictionaries in a dictionary, keyed by nodes:
            # distances_dict[each_node][connected_node] = weighting

            printable_dict_of_distances[each_node.value] \
                = printable_dict_for_edges_of_this_node

        # References used for the following section:
        # http://jlmedina123.wordpress.com
        #                 /2014/05/17/dijkstras-algorithm-in-python/
        # http://interactivepython.org
        #          /runestone/static/pythonds/Graphs/graphshortpath.html
        # http://rosettacode.org/wiki/Dijkstra%27s_algorithm

        # priority_queue = PriorityQueue()


        paths_from_the_start = {}

        for each_node in self.node_list:
            paths_from_the_start[each_node] = {'distance_so_far': 'infinity', 'previously_visited_node': None}


        # Try
        # http://www.eoinbailey.com/content/dijkstras-algorithm-illustrated-explanation



        distances_from_the_start = {}
        # previously_visited_nodes = []
        nodes_priority_queue = PriorityQueue

        paths_from_the_start[starting_node]['distance_so_far'] = 0

        previously_visited_nodes = []

        queue_to_visit = Queue()
        queue_to_visit.put(starting_node)

        current_node = None

        while queue_to_visit.qsize() > 0:

            current_node = queue_to_visit.get()

            previously_visited_nodes.append(current_node)

            edges_visited_this_step = []

            # Pseudonymizing...
            current_node_distance = paths_from_the_start[current_node]['distance_so_far']

            # Spreading from the current node:
            for each_edge in current_node.edges_for_this_node:
                # Pseudonymize the other node in the edge:
                the_other_node = other_node(current_node, each_edge)

                # Pseudonymizing...
                distance_for_traveling_to_this_other_node_from_current_node = (current_node_distance + each_edge.weighting)
                other_node_distance_so_far = paths_from_the_start[the_other_node]['distance_so_far']

                # Correcting infinities/updating nonvisited nodes to visited:
                if other_node_distance_so_far == 'infinity':
                    paths_from_the_start[the_other_node]['distance_so_far'] = distance_for_traveling_to_this_other_node_from_current_node

                    print("{} !!!! {}".format(current_node.value, paths_from_the_start[the_other_node]))

                    paths_from_the_start[the_other_node]['previously_visited_node'] = current_node.value  # debug

                    #other_node_distance_so_far = distance_for_traveling_to_this_other_node_from_current_node

                #if the_other_node not in previously_visited_nodes:

                #    previously_visited_nodes.append(the_other_node)

                # If we've found a shorter route to this node, update it:
                else:


                    if distance_for_traveling_to_this_other_node_from_current_node < other_node_distance_so_far:
                        paths_from_the_start[the_other_node]['distance_so_far'] = distance_for_traveling_to_this_other_node_from_current_node

                        print("{} !??! {}".format(current_node.value, paths_from_the_start[the_other_node]))

                        paths_from_the_start[the_other_node]['previously_visited_node'] = current_node.value  # debug

                #if the_other_node not in previously_visited_nodes:

                edges_visited_this_step.append([the_other_node, each_edge])

            sorted(edges_visited_this_step, key=lambda each_list: each_list[1])

            for each_node_edge_pair in edges_visited_this_step:

                if each_node_edge_pair[0] not in previously_visited_nodes:
                    queue_to_visit.put(each_node_edge_pair[0])





            # Next, put them all in the queue in order of lowest weighting first:

            # todo



        if current_node == ending_node:
            print("Success!\n    starting_node == {}\n    current_node == {}\n    ending_node == {}".format(starting_node.value, current_node.value, ending_node.value))




        print("printable_dict_of_distances == " + str(printable_dict_of_distances))

        # printable_paths_from_the_start = {}

        # for each_node in paths_from_the_start:
        #     if each_node is None:
        #         print("Error.")
        #     else:
        #         for each_subkey in paths_from_the_start[each_key]:
        #             if each_subkey is None:
        #                 print("ERROR!")
        #             else:
        #                 printable_paths_from_the_start[each_node.value][each_subkey.value] =


        # printable_paths_from_the_start = {key: value for key in dict}

        for each_key in paths_from_the_start:
            print("Node {}:\n    {}".format(each_key.value, paths_from_the_start[each_key]))






    def dijkstra_two(self, start, end):



        # The trivial case.
        if start == end:
            return [start]

        try:
            starting_node = self._return_node_with_this_value(start)
            ending_node = self._return_node_with_this_value(end)
        except:
            raise ValueError("Cannot path between {} and {}:"
                             " no such Node(s)".format(start, end))


        distances_from_the_start = {}

        priority_queue_to_visit = PriorityQueue()

        # I made the mistake of making these identical on one of my tries...
        dict_of_which_nodes_were_visited_before_which = {}
        already_pathed_nodes_list = []

        dict_of_which_nodes_were_visited_before_which[starting_node] = None

        # Put the starting node in the graph as the node with the lowest
        # distance away from the starting node.
        priority_queue_to_visit.put((0, starting_node))

        distances_from_the_start[starting_node] = 0

        # When nothing has been added to the priority queue in a given pass
        # and everything added before has been removed, there is nothing
        # left to check.
        while priority_queue_to_visit.qsize() > 0:

            # Take the node out of the graph with the lowest distance
            # away from the starting node.
            current_node = priority_queue_to_visit.get()[1]

            # Make sure you only do this for nodes that have been
            # the current_node!
            already_pathed_nodes_list.append(current_node)

            for each_edge in current_node.edges_for_this_node:

                # Pseudonym
                the_other_node = other_node(current_node, each_edge)

                if the_other_node in already_pathed_nodes_list:
                    # I'm so glad I learned about continue.
                    continue

                distance_for_traveling_to_this_other_node_from_current_node = distances_from_the_start[current_node] + each_edge.weighting



                if the_other_node in distances_from_the_start:

                    if distances_from_the_start[the_other_node] > distance_for_traveling_to_this_other_node_from_current_node:
                        distances_from_the_start[the_other_node] = distance_for_traveling_to_this_other_node_from_current_node
                        dict_of_which_nodes_were_visited_before_which[the_other_node] = current_node
                        priority_queue_to_visit.put((distances_from_the_start[the_other_node], the_other_node))
                else:
                    distances_from_the_start[the_other_node] = distance_for_traveling_to_this_other_node_from_current_node
                    dict_of_which_nodes_were_visited_before_which[the_other_node] = current_node
                    priority_queue_to_visit.put((distances_from_the_start[the_other_node], the_other_node))


        if ending_node not in distances_from_the_start:
            print "End node unreachable from start node."
            return


        # This next while loop creeps back through the dict of which nodes
        # were visited before each other and builds the shortest path.
        the_node_to_look_at_now = ending_node
        ordered_path_list = []

        while the_node_to_look_at_now is not None:

            ordered_path_list.insert(0, the_node_to_look_at_now.value)

            the_node_to_look_at_now = dict_of_which_nodes_were_visited_before_which[the_node_to_look_at_now]

        print "Distance: " + str(distances_from_the_start[ending_node]) + "\n" + str(ordered_path_list)

















def other_node(this_node, the_edge):
    if the_edge.alpha_node == this_node:
        return the_edge.beta_node
    else:
        return the_edge.alpha_node









from shortest_paths import ShortestPathsGraph

somewhat_complicated_graph = ShortestPathsGraph()

for each_integer in range(0, 10):
    somewhat_complicated_graph.add_node(each_integer)

# range(0, 10) gives 0 though 9 and len(that) gives 10
# for each_index in range(1, len(somewhat_complicated_graph.node_list)):
#     somewhat_complicated_graph.add_weighted_edge((each_index - 1), each_index, (each_index * 2))

for each_index in range(1, len(somewhat_complicated_graph.node_list)):
    somewhat_complicated_graph.add_weighted_edge((each_index - 1),
                                                 each_index, 1)


# Tie the graph chain together at the ends, making a circle:
somewhat_complicated_graph.add_weighted_edge(0, (len(somewhat_complicated_graph
                                             .node_list) - 1), 20)

print("\nfrom 0 to 5:")
#somewhat_complicated_graph.dijkstra_algorithm(0, 5)
somewhat_complicated_graph.dijkstra_two(0, 5)

print("\nfrom alpha to delta:")


simple_graph = ShortestPathsGraph()

simple_graph.add_weighted_edge("alpha", "beta", 1)
# Testing decision making capability of this algorithm can be as easy
# as flipping this particular number from huge to small:
simple_graph.add_weighted_edge("beta", "gamma", 199999999999)
simple_graph.add_weighted_edge("gamma", "delta", 1)
simple_graph.add_weighted_edge("hoopa", "gamma", 84)

simple_graph.add_weighted_edge("hoopa", "doopa", 646552)
simple_graph.add_weighted_edge("doopa", "loopa", 534)
# Or simply commenting this connection:
simple_graph.add_weighted_edge("alpha", "loopa", 1)

#simple_graph.dijkstra_algorithm("alpha", "delta")
simple_graph.dijkstra_two("alpha", "delta")



# print("0 to 4")

# square_graph =ShortestPathsGraph()

# for each_x in range(0, 5):


#     for each_y in range(0, 5):

#         if each_x > 0:
#             square_graph.add_weighted_edge(each_x - 1, each_y, abs(each_x - each_y))
#         if each_x < 5:
#             square_graph.add_weighted_edge(each_x + 1, each_y, abs(each_x - each_y))

#         if each_y > 0:
#             square_graph.add_weighted_edge(each_x, each_y - 1, abs(each_x - each_y))
#         if each_y < 5:
#             square_graph.add_weighted_edge(each_x, each_y + 1, abs(each_x - each_y))

# square_graph.dijkstra_algorithm(0, 4)












if __name__ == '__main__':
    # "In addition, write some demonstration code in
    # an "if __name__ == '__main__':" block at the end of your file
    # that shows how the two methods of traversal compare to each other
    # when performed on the same graph.
    # See if you can demonstrate the performance characteristics
    # of the two methods over a variety of graph orders."

    somewhat_complicated_graph = ShortestPathsGraph()

    for each_integer in range(0, 10):
        somewhat_complicated_graph.add_node(each_integer)

    # range(0, 10) gives 0 though 9 and len(that) gives 10
    for each_index in range(1, len(somewhat_complicated_graph.node_list)):
        somewhat_complicated_graph.add_edge((each_index - 1), each_index)

    # Tie the graph chain together at the ends, making a circle:
    somewhat_complicated_graph.add_edge(0, (len(somewhat_complicated_graph
                                                .node_list) - 1))

    # Connect to circle:
    somewhat_complicated_graph.add_edge("alpha", 4)
    somewhat_complicated_graph.add_node("alpha")

    # Side branch:
    somewhat_complicated_graph.add_node("omega")
    somewhat_complicated_graph.add_edge("omega", "alpha")

    # Deep branch:
    somewhat_complicated_graph.add_node("beta")
    somewhat_complicated_graph.add_node("gamma")
    somewhat_complicated_graph.add_node("delta")
    somewhat_complicated_graph.add_node("eta")
    somewhat_complicated_graph.add_node("theta")

    somewhat_complicated_graph.add_edge("alpha", "beta")
    somewhat_complicated_graph.add_edge("beta", "gamma")
    somewhat_complicated_graph.add_edge("gamma", "delta")
    somewhat_complicated_graph.add_edge("delta", "eta")

    # Extra side branch:
    somewhat_complicated_graph.add_edge("gamma", "theta")

    # Tie-backs:
    somewhat_complicated_graph.add_edge("gamma", 8)
    somewhat_complicated_graph.add_edge("theta", 8)

    # Minibranch:
    somewhat_complicated_graph.add_node("omicron")
    somewhat_complicated_graph.add_edge("omicron", 6)

    # Separated from the graph:
    somewhat_complicated_graph.add_node("upsilon")
    somewhat_complicated_graph.add_node("xi")
    somewhat_complicated_graph.add_edge("xi", "upsilon")

    print("\nDepth-first traversal:\n    ")
    print(somewhat_complicated_graph.depth_first_traversal("alpha"))

    print("\nBreadth-first traversal:\n    ")
    print(somewhat_complicated_graph.breadth_first_traversal("alpha"))

    check_if_random_is_okay = raw_input(
        "\n\nThe following code will generate numerous random graphs with"
        " unpredictable\ntopologies and print the results of calling both"
        " path functions to the console."
        "\n\nThis can be fairly spammy. If this is not desired, interrupt"
        " the program with\ncontrol-c."
        " Otherwise, press enter to continue . . .\n> ")

    # Mad science
    import random

    print("\n\n. . . Beginning random graph generation . . .\n")

    # Performance differences can be demonstrated by reducing the top
    # end of each_pass's range to 1, increasing the top and bottom of
    # random_node_count's range to >10000, and running the program
    # a few times to test different Graph types.
    for each_pass in range(0, 100):

        random_graph = ShortestPathsGraph()
        random_node_count = random.randint(10, 100)
        # -1 to allow for single-node graphs
        random_edge_count = random.randint(((random_node_count // 2) - 1),
                                           (random_node_count - 1))

        for each_node_count in range(0, random_node_count):
            random_graph.add_node(each_node_count)

        for each_edge_count in range(0, random_edge_count):
            # This graph is by no means guaranteed to be fully connected.
            two_random_nodes = random.sample(random_graph.node_list, 2)
            # Note to self: add_edge() is supposed to take values, not Nodes.
            random_graph.add_edge(two_random_nodes[0].value,
                                  two_random_nodes[1].value)

        random_edge = random.sample(random_graph.edge_list, 1)[0]
        random_connected_node = random_edge.alpha_node

        print "\n. Random Graph #{} .".format(each_pass)

        print "Depth-first traversal:\n    "
        print random_graph.depth_first_traversal(random_connected_node.value)

        print "\nBreadth-first traversal:\n    "
        print random_graph.breadth_first_traversal(random_connected_node.value)

    somewhat_complicated_graph = ShortestPathsGraph()

    for each_integer in range(0, 10):
        somewhat_complicated_graph.add_node(each_integer)

    # range(0, 10) gives 0 though 9 and len(that) gives 10
    for each_index in range(1, len(somewhat_complicated_graph.node_list)):
        somewhat_complicated_graph.add_edge((each_index - 1), each_index)
