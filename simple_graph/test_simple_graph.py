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
            self.linear_graph.add_node(Node())
        for each_node in range(1, len(self.linear_graph.node_list)):
            self.linear_graph.add_edge(
                Edge(self.linear_graph.node_list[each_node],
                     self.linear_graph.node_list[(each_node + 1)]))

        self.circular_graph = simple_graph.Graph()

        for each_integer in range(0, 10):
            self.circular_graph.add_node(Node())
        for each_node in range(1, len(self.circular_graph.node_list)):
            self.circular_graph.add_edge(
                Edge(self.circular_graph.node_list[each_node],
                     self.circular_graph.node_list[(each_node + 1)]))
        # Tie it together:
        self.circular_graph.add_edge(
            self.circular_graph.node_list[0],
            self.circular_graph.node_list[
                (len(self.circular_graph.node_list) - 1)
            ])

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

        self.setUp()

        empty_graph_nodes = self.empty_graph.nodes()
        linear_graph_nodes = self.linear_graph.nodes()
        circular_graph_nodes = self.circular_graph.nodes()

        assert len(empty_graph_nodes) == 0
        assert isinstance(empty_graph_nodes, list)
        assert len(linear_graph_nodes) == 10
        assert isinstance(linear_graph_nodes, list)
        assert len(circular_graph_nodes) == 10
        assert isinstance(cicular_graph_nodes, list)

    def test_edges(self):

        self.setUp()

        empty_graph_edges = self.empty_graph.edges()
        linear_graph_edges = self.linear_graph.edges()
        circular_graph_edges = self.circular_graph.edges()

        assert len(empty_graph_edges) == 0
        assert isinstance(empty_graph_edges, list)
        assert len(linear_graph_edges) == 10
        assert isinstance(linear_graph_edges, list)
        assert len(circular_graph_edges) == 11
        assert isinstance(cicular_graph_edges, list)

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
        for each_integer in range(0, 3):
            node_to_delete = self.linear_graph.nodes[each_integer]
            node_to_delete.value = each_integer  # 0, 1, 2
            deleted_linear_graph_nodes.append(node_to_delete.value)
            self.linear_graph.del_node(
                self.linear_graph.nodes[each_integer])

        deleted_circular_graph_nodes = []
        for each_integer in range(0, 3):
            node_to_delete = self.circular_graph.nodes[each_integer]
            node_to_delete.value = each_integer  # 0, 1, 2
            deleted_circular_graph_nodes.append(
                node_to_delete.value)  # [0, 1, 2]
            self.circular_graph.del_node(
                self.circular_graph.nodes[each_integer])

        linear_graph_nodes = self.linear_graph.nodes()
        circular_graph_nodes = self.circular_graph.nodes()

        for each_node in linear_graph_nodes:
            assert each_node.value not in deleted_linear_graph_nodes
        for each_node in circular_graph_nodes:
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

        deleted_linear_graph_nodes = []
        for each_integer in range(0, 3):
            edge_to_delete = self.linear_graph.edges[each_integer]
            edge_to_delete.value = each_integer  # 0, 1, 2
            deleted_linear_graph_edges.append(edge_to_delete.value)
            self.linear_graph.del_edge(
                self.linear_graph.edges[each_integer])

        deleted_circular_graph_nodes = []
        for each_integer in range(0, 3):
            edge_to_delete = self.circular_graph.edges[each_integer]
            edge_to_delete.value = each_integer  # 0, 1, 2
            deleted_circular_graph_edges.append(
                edge_to_delete.value)  # [0, 1, 2]
            self.circular_graph.del_edge(
                self.circular_graph.edges[each_integer])

        # Make sure the Edges are not in the Graph:
        linear_graph_edges = self.linear_graph.edges()
        circular_graph_edges = self.circular_graph.edges()

        for each_edge in linear_graph_edges:
            assert each_edge.value not in deleted_linear_graph_edges
        for each_edge in circular_graph_edges:
            assert each_edge.value not in deleted_circular_graph_edges

        # Now make sure the Edges are also not in the Nodes:
        linear_graph_nodes = self.linear_graph.nodes()
        circular_graph_nodes = self.circular_graph.nodes()

        for each_node in linear_graph_nodes:
            for each_deleted_edge in deleted_linear_graph_edges:
                assert each_deleted_edge not in linear_graph_nodes.edges
        for each_node in circular_graph_nodes:
            for each_deleted_edge in deleted_circular_graph_edges:
                assert each_deleted_edge not in circular_graph_nodes.edges


    def test_has_node(self):
        ''' g.has_node(n): True if node 'n' is
        contained in the graph, False if not. '''

        self.setUp()


        with self.assertRaises(Exception):
            self.empty_graph.has_node()
        with self.assertRaises(Exception):
            self.empty_graph.has_node(1)
        with self.assertRaises(Exception):
            self.empty_graph.has_node(Edge())

        with self.assertRaises(Exception):
            self.linear_graph.has_node()
        with self.assertRaises(Exception):
            self.linear_graph.has_node(1)
        with self.assertRaises(Exception):
            self.linear_graph.has_node(Edge())

        with self.assertRaises(Exception):
            self.circular_graph.has_node()
        with self.assertRaises(Exception):
            self.circular_graph.has_node(1)
        with self.assertRaises(Exception):
            self.circular_graph.has_node(Edge())

        for each_node_it_has in self.linear_graph.nodes():
            assert self.linear_graph.has_node(each_node_it_has)
        for each_node_it_has in self.circular_graph.nodes():
            assert self.circular_graph.has_node(each_node_it_has)


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
            self.linear_graph.neighbors(1)
        with self.assertRaises(Exception):
            self.linear_graph.neighbors(Edge())

        with self.assertRaises(Exception):
            self.circular_graph.neighbors()
        with self.assertRaises(Exception):
            self.circular_graph.neighbors(1)
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

        # Construct a new linear graph to test on, using the empty graph.
        # In order to distinguish between Nodes in an order that is not
        # tied to list order after the Nodes have been sitting in it for
        # a while, we must have a secondary method of determining Edge
        # concatenation.
        # For this purpose we will use serial integers related to Node
        # addition as it was at the time the Graph was compiled.
        # First, put in the special node which appears before any neighbors:
        list_of_added_nodes = []
        first_node = Node()
        first_node.value = 0
        list_of_added_nodes.append(first_node)
        self.empty_graph.add_node(first_node)

        # Add new nodes connected with Edges to the immediately previous Node:
        for each_integer in range(1, 10):
            new_node = Node()
            new_node.value = each_integer
            new_edge = Edge(new_node, list_of_added_nodes[(each_integer - 1)])
            list_of_added_nodes.append(new_node)
            self.empty_graph.add_node(new_node)
            self.empty_graph.add_edge(new_edge)

        # Now, verify particular Nodes are consistently
        # connected via particular Edges.
        # To do this, we're taking advantage of the fact that
        # previously instantiated Nodes were related to each other
        # at the time of creation by their order in the temporary list.
        for each_node in self.empty_graph.nodes():
            for each_neighbor in each_node.neighbors():
                # Disallow edge cases; this is linear, not circular.
                if each_node.value != 0 and each_neighbor.value != 10:
                    assert abs(each_node.value - each_neighbor.value) == 1



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

        new_node_one = Node()
        new_node_two = Node()
        new_node_three = Node()
        new_node_four = Node()

        self.empty_graph.add_node(new_node_one)
        self.empty_graph.add_node(new_node_two)
        self.empty_graph.add_node(new_node_three)
        self.empty_graph.add_node(new_node_four)

        new_edge_one = Edge(new_node_one, new_node_two)
        new_edge_two = Edge(new_node_two, new_node_three)
        new_edge_three = Edge(new_node_three, new_node_four)
        new_edge_four = Edge(new_node_four, new_node_one)

        self.empty_graph.add_edge(new_edge_one)
        self.empty_graph.add_edge(new_edge_two)
        self.empty_graph.add_edge(new_edge_three)
        self.empty_graph.add_edge(new_edge_four)

        assert self.empty_graph.adjacent(new_node_one, new_node_two) is True
        assert self.empty_graph.adjacent(new_node_two, new_node_three) is True
        assert self.empty_graph.adjacent(new_node_three, new_node_four) is True
        assert self.empty_graph.adjacent(new_node_four, new_node_one) is True

        assert self.empty_graph.adjacent(new_node_one, new_node_three) is False
        assert self.empty_graph.adjacent(new_node_two, new_node_four) is False
        assert self.empty_graph.adjacent(new_node_three, new_node_one) is False
        assert self.empty_graph.adjacent(new_node_four, new_node_two) is False

