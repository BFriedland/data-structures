

from Queue import Queue, PriorityQueue


class Node:

    def __init__(self, value):

        self.value = value
        self.edges_for_this_node = []

        # For the A* algorithm; optional in all other cases.
        self.x_coordinate = None
        self.y_coordinate = None


class Edge:

    def __init__(self, alpha_node, beta_node):

        self.alpha_node = alpha_node
        self.beta_node = beta_node

        # For Dijkstra's and A*:
        self.weighting = None


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
        '''
        Uses Dijkstra's algorithm to calculate the shortest path
        between two nodes in the graph, supplied to this algorithm
        as the starting and ending nodes' values.
        '''

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

            # Take the node out of the priority queue with
            # the lowest distance away from the starting node.
            current_node = priority_queue_to_visit.get()[1]

            # Make sure you only do this for nodes that have been
            # the current_node!
            already_pathed_nodes_list.append(current_node)

            for each_edge in current_node.edges_for_this_node:

                # Pseudonymize
                the_other_node = self.other_node(current_node, each_edge)

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
            return None

        # This next while loop creeps back through the dict of which nodes
        # were visited before each other and builds the shortest path.
        the_node_to_look_at_now = ending_node
        ordered_path_list = []

        while the_node_to_look_at_now is not None:

            ordered_path_list.insert(0, the_node_to_look_at_now.value)

            the_node_to_look_at_now = dict_of_which_nodes_were_visited_before_which[the_node_to_look_at_now]

        return distances_from_the_start[ending_node], ordered_path_list

    def a_star_algorithm(self, start, end, heuristic=None):

        # The A* algorithm is very similar to Dijkstra's algorithm.
        # This is because the A* algorithm is an improvement upon
        # Dijkstra's algorithm, adding a step that consults a heuristic
        # to determine which nodes to check next. This heuristic can,
        # if properly chosen, increase the efficiency with which the
        # shortest path may be found.

        # Developed with reference to:
        # http://en.wikipedia.org/wiki/A*_search_algorithm
        # Some insight from:
        # http://code.activestate.com
        #      /recipes/577519-a-star-shortest-path-algorithm/

        if heuristic is None:
            heuristic = self.default_heuristic

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
        guesses_for_distances_from_the_start = {}

        priority_queue_to_visit = PriorityQueue()

        dict_of_which_nodes_were_visited_before_which = {}
        already_pathed_nodes_list = []

        dict_of_which_nodes_were_visited_before_which[starting_node] = None

        # Put the starting node in the graph as the node with the lowest
        # distance away from the starting node.
        priority_queue_to_visit.put((0, starting_node))

        distances_from_the_start[starting_node] = 0
        guesses_for_distances_from_the_start[starting_node] = distances_from_the_start[starting_node] + heuristic(starting_node, ending_node)

        # When nothing has been added to the priority queue in a given pass
        # and everything added before has been removed, there is nothing
        # left to check.
        while priority_queue_to_visit.qsize() > 0:

            # Take the node out of the priority queue with
            # the lowest distance away from the starting node.
            # For the A* algorithm, note that the priority queue
            # has already been sorted according to guessed distances.
            current_node = priority_queue_to_visit.get()[1]
            already_pathed_nodes_list.append(current_node)

            for each_edge in current_node.edges_for_this_node:

                # Pseudonymize
                the_other_node = self.other_node(current_node, each_edge)

                if the_other_node in already_pathed_nodes_list:
                    continue

                distance_for_traveling_to_this_other_node_from_current_node = distances_from_the_start[current_node] + each_edge.weighting

                if the_other_node in distances_from_the_start:

                    if distances_from_the_start[the_other_node] > distance_for_traveling_to_this_other_node_from_current_node:
                        distances_from_the_start[the_other_node] = distance_for_traveling_to_this_other_node_from_current_node
                        dict_of_which_nodes_were_visited_before_which[the_other_node] = current_node
                        # A* algorithm's differentiation step:
                        guesses_for_distances_from_the_start[the_other_node] = distances_from_the_start[the_other_node] + heuristic(the_other_node, ending_node)
                        # Note that the heuristically-informed guess is what
                        # the priority queue is sorted by.
                        priority_queue_to_visit.put((guesses_for_distances_from_the_start[the_other_node], the_other_node))
                else:
                    distances_from_the_start[the_other_node] = distance_for_traveling_to_this_other_node_from_current_node
                    dict_of_which_nodes_were_visited_before_which[the_other_node] = current_node
                    # A* algorithm's differentiation step:
                    guesses_for_distances_from_the_start[the_other_node] = distances_from_the_start[the_other_node] + heuristic(the_other_node, ending_node)
                    # Note that the heuristically-informed guess is what
                    # the priority queue is sorted by.
                    priority_queue_to_visit.put((guesses_for_distances_from_the_start[the_other_node], the_other_node))

        if ending_node not in distances_from_the_start:
            return None

        # This next while loop creeps back through the dict of which nodes
        # were visited before each other and builds the shortest path.
        the_node_to_look_at_now = ending_node
        ordered_path_list = []

        while the_node_to_look_at_now is not None:

            ordered_path_list.insert(0, the_node_to_look_at_now.value)

            the_node_to_look_at_now = dict_of_which_nodes_were_visited_before_which[the_node_to_look_at_now]

        # Important!
        # The A* algorithm does NOT use guesses_for_distances_from_the_start
        # when returning the path.
        # The actual distance from the start determines what route to take;
        # the heuristic modifier only changes how fast it finds it.
        return distances_from_the_start[ending_node], ordered_path_list

    def other_node(self, this_node, the_edge):
        if the_edge.alpha_node == this_node:
            return the_edge.beta_node
        else:
            return the_edge.alpha_node

    def default_heuristic(self, *args, **kwargs):
        # In the A* algorithm, the heuristic is supposed to be a guess about
        # the ideal direction to head in that informs the choice of which
        # node to check next when finding paths through the graph.
        # On a realistic 2d graph this would be the "Euclidean" distance,
        # or sqrt(x^2 + y^2) away from the goal.
        # For some more symbolically-connected graphs the "Manhattan" and
        # "Chebyshev" heuristics can be used, which seem like they're
        # intended for estimating based on moving in straight lines and
        # making right angle turns (Manhattan) or moving node to node
        # with predictable distances but without regard for the Euclidean
        # distance modifier (Chebyshev).

        # References:
        # http://code.activestate.com
        #      /recipes/577519-a-star-shortest-path-algorithm/
        # http://en.wikipedia.org/wiki/Euclidean_distance
        # http://en.wikipedia.org/wiki/Taxicab_geometry
        # http://en.wikipedia.org/wiki/Chebyshev_distance

        # Graphs with regular distances and absolute directions have
        # meaningful heuristics, but my ShortestPathsGraph's bare-minimum
        # default configuration cannot assume it will be made with anything
        # like X and Y mapping or uniform distances between nodes, so
        # instead of making it process meaningless numbers, I'll hand it zero.
        # Other geometries may warrant different heuristics, and my
        # implementation of the A* algorithm is ready to handle them
        # using helper methods other than the default.
        return 0

    # Note that the following heuristics are meaningless without support
    # for Cartesian coordinates, which is an end-user thing, far removed
    # from the realm of pure logic my graph prefers to live in.

    def euclidean_heuristic(self, starting_node, ending_node):
        # For graphs intending to use Euclidean geometry to find paths.
        x_difference = ending_node.x_coordinate - starting_node.x_coordinate
        y_difference = ending_node.y_coordinate - starting_node.y_coordinate

        import math
        return math.sqrt((x_difference ** 2) + (y_difference ** 2))

    def manhattan_heuristic(self, starting_node, ending_node):
        # For graphs using Cartesian coordinates in which you may only
        # travel in orthogonal lines between nodes.
        x_difference = ending_node.x_coordinate - starting_node.x_coordinate
        y_difference = ending_node.y_coordinate - starting_node.y_coordinate

        return (abs(x_difference) + abs(y_difference))

    def chebyshev_heuristic(self, starting_node, ending_node):
        # For graphs using Cartesian coordinates where movement between
        # nodes can happen diagonally, and that movement incurs the same
        # cost as moving orthogonally (e.g. chess).
        x_difference = ending_node.x_coordinate - starting_node.x_coordinate
        y_difference = ending_node.y_coordinate - starting_node.y_coordinate

        return max(abs(x_difference), abs(y_difference))


if __name__ == '__main__':

    graph_zero = ShortestPathsGraph()

    for each_integer in range(0, 10):
        graph_zero.add_node(each_integer)

    # range(0, 10) gives 0 though 9 and len(that) gives 10
    # for each_index in range(1, len(graph_zero.node_list)):
    #     # For values that scale from one part of the graph to another:
    #     graph_zero.add_weighted_edge((each_index - 1), each_index, (each_index * 2))

    for each_index in range(1, len(graph_zero.node_list)):
        graph_zero.add_weighted_edge((each_index - 1),
                                                     each_index, 1)

    # Tie the graph chain together at the ends, making a circle:
    graph_zero.add_weighted_edge(0, (len(graph_zero
                                                 .node_list) - 1), 20)

    print "\nfrom 0 to 5:"
    print "Dijkstra's: " + str(graph_zero.dijkstra_algorithm(0, 5))
    print "A*: " + str(graph_zero.a_star_algorithm(0, 5))
    print "from 9 to 5:"
    print "Dijkstra's: " + str(graph_zero.dijkstra_algorithm(9, 5))
    print "A*: " + str(graph_zero.a_star_algorithm(9, 5))

    print "\nfrom alpha to delta:"

    graph_one = ShortestPathsGraph()

    graph_one.add_weighted_edge("alpha", "beta", 1)
    # Testing decision making capability of this algorithm can be as easy
    # as flipping this particular number from huge to small:
    graph_one.add_weighted_edge("beta", "gamma", 199999999999)
    graph_one.add_weighted_edge("gamma", "delta", 1)
    graph_one.add_weighted_edge("hoopa", "gamma", 84)

    graph_one.add_weighted_edge("hoopa", "doopa", 646552)
    graph_one.add_weighted_edge("doopa", "loopa", 534)
    # Or simply commenting this connection:
    graph_one.add_weighted_edge("alpha", "loopa", 1)

    print "Dijkstra's: " + str(graph_one.dijkstra_algorithm("alpha", "delta"))
    print "A*: " + str(graph_one.a_star_algorithm("alpha", "delta"))

    print "with beta-gamma bypass:"
    # The algorithms work properly even with multiple edges per vertex pair:
    graph_one.add_weighted_edge("beta", "gamma", 1)

    print "Dijkstra's: " + str(graph_one.dijkstra_algorithm("alpha", "delta"))
    print "A*: " + str(graph_one.a_star_algorithm("alpha", "delta"))

    print "\nalpha to separated node:"
    # Separated:
    graph_one.add_node("omicron")

    print "Dijkstra's: " + str(graph_one.dijkstra_algorithm("alpha", "omicron"))
    print "A*: " + str(graph_one.a_star_algorithm("alpha", "omicron"))
