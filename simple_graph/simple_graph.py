
class Node:

    def __init__(self, value):

        self.value = value
        self.edges_for_this_node = []


class Edge:

    def __init__(self, alpha_node, beta_node):

        self.alpha_node = alpha_node
        self.beta_node = beta_node


class Graph:

    def __init__(self):

        self.node_list = []
        self.edge_list = []

    def nodes(self):
        ''' Return a list containing all Nodes in the Graph. '''

        node_list_to_return = []
        for each_node in self.node_list:
            node_list_to_return.append(each_node.value)
        return node_list_to_return

    def edges(self):
        ''' Return a list containing the Node values
        of every Edge in the Graph contained in separate
        tuples within the returned list.. '''

        edge_list_to_return = []
        for each_edge in self.edge_list:
            alpha_node = each_edge.alpha_node
            beta_node = each_edge.beta_node
            node_tuple = (alpha_node, beta_node)
            edge_list_to_return.append(node_tuple)

        return edge_list_to_return

    def add_node(self, n, _returning=False):
        ''' Add a new Node with the value n to the Graph. '''

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

            raise Exception("{} not in Graph".formate(n))

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
        from the Graph. Raise an exception if no such Edge exists. '''

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
            raise Exception("Edge ({}, {}) not in Graph".format(n1, n2))

    def neighbors(self, n):
        ''' Return the list of all Nodes connected to Node n by Edges.
        Raise an exception if n is not in the Graph. '''

        if self.has_node(n) is False:
            raise Exception("{} not in Graph.\nGraphlist: {}".format(n.value,
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
        Nodes are not in the Graph. '''

        if not self.has_node(n1):
            raise Exception("{} not in Graph".format(n1))

        if not self.has_node(n2):
            raise Exception("{} not in Graph".format(n2))

        for each_edge in self.edge_list:
            # Spread out and euonymized to make it easier to read:
            alpha_node_value = each_edge.alpha_node.value
            beta_node_value = each_edge.beta_node.value
            if (n1 == alpha_node_value) or (n1 == beta_node_value):
                if (n2 == alpha_node_value) or n2 == (beta_node_value):
                    return True
        return False




