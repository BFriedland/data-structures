
import unittest
import random

import traversable_graph


class test_TraversableGraph(unittest.TestCase):

    def test_both_traversals(self):

        # Random graphs have all the properties of predictable graphs,
        # and over a sufficiently large number of iterations they will
        # also test all the reasonable permutations of predictable graphs,
        # including ones with isolated vertices and webs.
        # This random graph code is demonstrated wordily by printing

        for each_pass in range(0, 100):

            random_graph = traversable_graph.TraversableGraph()
            random_node_count = random.randint(10, 100)
            # -1 to allow for single-node TraversableGraphs
            random_edge_count = random.randint(((random_node_count // 2) - 1),
                                               (random_node_count - 1))

            for each_node_count in range(0, random_node_count):
                random_graph.add_node(each_node_count)

            for each_edge_count in range(0, random_edge_count):
                # This graph is by no means guaranteed to be fully connected.
                two_random_nodes = random.sample(random_graph.node_list, 2)
                # Note to self: add_edge() takes values, not Nodes.
                random_graph.add_edge(two_random_nodes[0].value,
                                      two_random_nodes[1].value)

            random_edge = random.sample(random_graph.edge_list, 1)[0]
            random_connected_node = random_edge.alpha_node

            deep_path = random_graph.depth_first_traversal(
                random_connected_node.value)

            broad_path = random_graph.breadth_first_traversal(
                random_connected_node.value)

            # Ensure the paths are full of ints:
            assert isinstance(deep_path[0], int)
            assert isinstance(broad_path[0], int)

            # Ensure the paths are no longer than the number of nodes:
            assert len(deep_path) <= random_node_count
            assert len(broad_path) <= random_node_count

            # Ensure paths are nonzero:
            assert len(deep_path) > 0
            assert len(broad_path) > 0

            # If the length of each path is equal to the length of
            # itself after duplicates have been removed,
            # it does not have any repeated values,
            # meaning it visited each node at most only once.
            assert len(set(deep_path)) == len(deep_path)
            assert len(set(broad_path)) == len(broad_path)

            with self.assertRaises(Exception):
                random_graph.breadth_first_traversal("g")
                random_graph.depth_first_traversal("g")
                random_graph.breadth_first_traversal(-3)
                random_graph.depth_first_traversal(-3)

                # Note that this is only guaranteed for len(path) and higher:
                random_graph.breadth_first_traversal(len(broad_path))
                random_graph.depth_first_traversal(len(deep_path))

        # For reference...
        # Using the final random graph, this test should have
        # a noticeably uneven distribution of passes and failures
        # when tested multiple times:
        # random_graph.breadth_first_traversal(len(broad_path) - 15)

    # Testing the rest of TraversableGraph:

    def setUp(self):

        # Note: This test method tests add_edge(), add_node() and
        # the TraversableGraph constructor.

        self.empty_graph = traversable_graph.TraversableGraph()

        self.linear_graph = traversable_graph.TraversableGraph()
        for each_integer in range(0, 10):
            self.linear_graph.add_node(each_integer)
        # range(0, 10) gives 0 though 9 and len(that) gives 10
        for each_index in range(1, len(self.linear_graph.node_list)):
            self.linear_graph.add_edge((each_index - 1), each_index)

        self.circular_graph = traversable_graph.TraversableGraph()
        for each_integer in range(0, 10):
            self.circular_graph.add_node(each_integer)
        # range(0, 10) gives 0 though 9 and len(that) gives 10
        for each_index in range(1, len(self.circular_graph.node_list)):
            self.circular_graph.add_edge((each_index - 1), each_index)
        # Tie the graph chain together at the ends:
        self.circular_graph.add_edge(0, (len(self.circular_graph.node_list)-1))

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

        # This also tests add_edge()

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

        # Make sure the Edges are not in the TraversableGraph:
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
        # Additional required test case: Node-type not in TraversableGraph
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
