import simple_graph
import unittest

'''
Your graph should support the following operations:

g.nodes(): return a list of all nodes in the graph
g.edges(): return a list of all edges in the graph
g.add_node(n): adds a new node 'n' to the graph
g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2',
    if either n1 or n2 are not already present in the graph, they should
    be added.
g.del_node(n): deletes the node 'n' from the graph, raises an error if no
    such node exists
g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the
    graph, raises an error if no such edge exists
g.has_node(n): True if node 'n' is contained in the graph, False if not.
g.neighbors(n): returns the list of all nodes connected to 'n' by edges,
    raises an error if n is not in g
g.adjacent(n1, n2): returns True if there is an edge connecting n1 and
    n2, False if not, raises an error if either of the supplied nodes
    are not in g
'''


class test_Graph(unittest.TestCase):

    def setUp(self):

        # Note: This test method tests add_edge(), add_node() and
        # the Graph constructor.

        self.empty_graph = simple_graph.Graph()

        self.linear_graph = simple_graph.Graph()
        for each_integer in range(0, 10):
            self.linear_graph.add_node(each_integer)
        # range(0, 10) gives 0 though 9 and len(that) gives 10
        for each_index in range(1, len(self.linear_graph.node_list)):
            self.linear_graph.add_edge((each_index - 1), each_index)

        self.circular_graph = simple_graph.Graph()
        for each_integer in range(0, 10):
            self.circular_graph.add_node(each_integer)
        # range(0, 10) gives 0 though 9 and len(that) gives 10
        for each_index in range(1, len(self.circular_graph.node_list)):
            self.circular_graph.add_edge((each_index - 1), each_index)
        # Tie the graph chain together at the ends:
        self.circular_graph.add_edge(0, (len(self.circular_graph.node_list)-1))

        # I just realized why I hate making test cases.
        # It's like writing functionality that nobody needs yet!
        # How do you know where to stop if the problem domain isn't
        # even defined yet?
        # This only makes sense if you know what you're building first,
        # and then only from the point of view that you already know the
        # logical boundaries of the problem domain and can reference
        # them directly.
        # Otherwise, it's writing code for something that won't be used
        # because the actual non-test program will require completely
        # rewriting the tests in order for the tests to work with it.
        # There must be something I don't know that would make writing
        # tests more straightforwards and obvious than writing the
        # thing I'm testing...

    def test_nodes(self):

        # This also tests add_node()

        self.setUp()

        empty_graph_nodes = self.empty_graph.nodes()
        linear_graph_nodes = self.linear_graph.nodes()
        circular_graph_nodes = self.circular_graph.nodes()

        assert len(empty_graph_nodes) == 0
        assert isinstance(empty_graph_nodes, list)
        assert len(linear_graph_nodes) == 10
        assert isinstance(linear_graph_nodes, list)
        assert len(circular_graph_nodes) == 10
        assert isinstance(circular_graph_nodes, list)

    def test_edges(self):

        ## This also tests add_edge()

        self.setUp()

        empty_graph_edges = self.empty_graph.edges()
        linear_graph_edges = self.linear_graph.edges()
        circular_graph_edges = self.circular_graph.edges()

        assert len(empty_graph_edges) == 0
        assert isinstance(empty_graph_edges, list)
        assert len(linear_graph_edges) == 9
        assert isinstance(linear_graph_edges, list)
        assert len(circular_graph_edges) == 10
        assert isinstance(circular_graph_edges, list)

    def test_has_node(self):
        ''' g.has_node(n): True if node 'n' is
        contained in the graph, False if not. '''

        self.setUp()

        assert self.empty_graph.has_node(1) is False

        with self.assertRaises(Exception):
            self.empty_graph.has_node()
        with self.assertRaises(Exception):
            self.empty_graph.has_node(Edge())

        with self.assertRaises(Exception):
            self.linear_graph.has_node()
        with self.assertRaises(Exception):
            assert self.linear_graph.has_node("1") is True
        with self.assertRaises(Exception):
            self.linear_graph.has_node(Edge())

        with self.assertRaises(Exception):
            self.circular_graph.has_node()
        with self.assertRaises(Exception):
            assert self.circular_graph.has_node("1") is True
        with self.assertRaises(Exception):
            self.circular_graph.has_node(Edge())

        for each_node_it_has in self.linear_graph.node_list:
            assert self.linear_graph.has_node(each_node_it_has.value)
        for each_node_it_has in self.circular_graph.node_list:
            assert self.circular_graph.has_node(each_node_it_has.value)





    def test_del_node(self):
        ''' g.del_node(n): deletes the node 'n' from the graph,
        raises an error if no such node exists '''

        self.setUp()

        with self.assertRaises(Exception):
            self.empty_graph.del_node('100')
        with self.assertRaises(Exception):
            self.empty_graph.del_node()
        with self.assertRaises(Exception):
            self.empty_graph.del_node(None)

        with self.assertRaises(Exception):
            self.linear_graph.del_node('100')
        with self.assertRaises(Exception):
            self.linear_graph.del_node()
        with self.assertRaises(Exception):
            self.linear_graph.del_node(None)

        with self.assertRaises(Exception):
            self.circular_graph.del_node('100')
        with self.assertRaises(Exception):
            self.circular_graph.del_node()
        with self.assertRaises(Exception):
            self.circular_graph.del_node(None)

        deleted_linear_graph_nodes = []
        for each_integer in range(100, 103):
            node_to_delete = self.linear_graph.add_node(each_integer,
                                                        _returning=True)
            deleted_linear_graph_nodes.append(node_to_delete.value)
            self.linear_graph.del_node(each_integer)

        deleted_circular_graph_nodes = []
        for each_integer in range(100, 103):
            node_to_delete = self.circular_graph.add_node(each_integer,
                                                          _returning=True)
            deleted_circular_graph_nodes.append(each_integer)
            self.circular_graph.del_node(each_integer)

        circular_graph_nodes = self.circular_graph.node_list

        for each_node in self.linear_graph.node_list:
            assert each_node.value not in deleted_linear_graph_nodes
        for each_node in self.circular_graph.node_list:
            assert each_node.value not in deleted_circular_graph_nodes

    def test_del_edge(self):
        ''' g.del_edge(n1, n2): deletes the edge connecting 'n1' and
        'n2' from the graph, raises an error if no such edge exists '''

        self.setUp()

        with self.assertRaises(Exception):
            self.empty_graph.del_edge('100')
        with self.assertRaises(Exception):
            self.empty_graph.del_edge()
        with self.assertRaises(Exception):
            self.empty_graph.del_edge(None)

        with self.assertRaises(Exception):
            self.linear_graph.del_edge('100')
        with self.assertRaises(Exception):
            self.linear_graph.del_edge()
        with self.assertRaises(Exception):
            self.linear_graph.del_edge(None)

        with self.assertRaises(Exception):
            self.circular_graph.del_edge('100')
        with self.assertRaises(Exception):
            self.circular_graph.del_edge()
        with self.assertRaises(Exception):
            self.circular_graph.del_edge(None)

        self.linear_graph.del_edge(1, 2)
        self.circular_graph.del_edge(1, 2)

        # Make sure the Edges are not in the Graph:
        for each_edge in self.linear_graph.edge_list:
            assert ((each_edge.alpha_node != 1)
                    and (each_edge.beta_node != 2))

        for each_edge in self.circular_graph.edge_list:
            assert ((each_edge.alpha_node != 1)
                    and (each_edge.beta_node != 2))

    def test_neighbors(self):

        ''' g.neighbors(n): returns the list of all nodes connected
        to 'n' by edges, raises an error if n is not in g '''

        self.setUp()

        with self.assertRaises(Exception):
            self.empty_graph.neighbors()
        with self.assertRaises(Exception):
            self.empty_graph.neighbors(1)
        with self.assertRaises(Exception):
            self.empty_graph.neighbors(Edge())

        with self.assertRaises(Exception):
            self.linear_graph.neighbors()
        with self.assertRaises(Exception):
            self.linear_graph.neighbors(11)
        with self.assertRaises(Exception):
            self.linear_graph.neighbors(Edge())

        with self.assertRaises(Exception):
            self.circular_graph.neighbors()
        with self.assertRaises(Exception):
            self.circular_graph.neighbors(11)
        with self.assertRaises(Exception):
            self.circular_graph.neighbors(Edge())

        # "raises an error if n is not in g"
        # Additional required test case: Node-type not in Graph
        with self.assertRaises(Exception):
            self.empty_graph.neighbors(Node())
        with self.assertRaises(Exception):
            self.linear_graph.neighbors(Node())
        with self.assertRaises(Exception):
            self.circular_graph.neighbors(Node())

        # Add new nodes connected with Edges to the immediately previous Node:
        for each_integer in range(0, 10):
            self.empty_graph.add_node(each_integer)
            self.empty_graph.add_edge(each_integer, (each_integer - 1))

        for each_node in self.empty_graph.node_list:
            # Without this line I'd be declaring .value in two lower lines...
            each_node_value = each_node.value
            # each_node.value is because neighbors() takes a value, not a Node.
            for each_neighbor_value \
               in self.empty_graph.neighbors(each_node_value):
                # If the neighbor values of a given value in an
                # int(1)-stepped list are all +/- 1,
                # then neighbors() works.
                assert abs(each_node_value - each_neighbor_value) == 1


    def test_adjacent(self):

        ''' g.adjacent(n1, n2): returns True if there is an edge
        connecting n1 and n2, False if not, raises an error if
        either of the supplied nodes are not in g '''

        self.setUp()

        with self.assertRaises(Exception):
            self.empty_graph.adjacent()
        with self.assertRaises(Exception):
            self.empty_graph.adjacent(1)
        with self.assertRaises(Exception):
            self.empty_graph.adjacent(Edge())

        with self.assertRaises(Exception):
            self.linear_graph.adjacent()
        with self.assertRaises(Exception):
            self.linear_graph.adjacent(1)
        with self.assertRaises(Exception):
            self.linear_graph.adjacent(Edge())

        with self.assertRaises(Exception):
            self.circular_graph.adjacent()
        with self.assertRaises(Exception):
            self.circular_graph.adjacent(1)
        with self.assertRaises(Exception):
            self.circular_graph.adjacent(Edge())

        self.empty_graph.add_node(1)
        self.empty_graph.add_node(2)
        self.empty_graph.add_node(3)
        self.empty_graph.add_node(4)

        self.empty_graph.add_edge(1, 2)
        self.empty_graph.add_edge(2, 3)
        self.empty_graph.add_edge(3, 4)
        self.empty_graph.add_edge(4, 1)

        assert self.empty_graph.adjacent(1, 2) is True
        assert self.empty_graph.adjacent(2, 3) is True
        assert self.empty_graph.adjacent(3, 4) is True
        assert self.empty_graph.adjacent(4, 1) is True

        assert self.empty_graph.adjacent(1, 3) is False
        assert self.empty_graph.adjacent(2, 4) is False



unittest.main()
