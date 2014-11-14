data-structures
===============

[![Build Status](https://travis-ci.org/BFriedland/data-structures.svg)](https://travis-ci.org/BFriedland/data-structures)

Sample code for classic data structures implemented in Python.

Includes implementations of linked list, queue, doubly-linked list,
    stack, binary heap, priority queue, binary search tree, and
    a simple graph structure.

Simple graphs behave as the computer science notion of a graph, containing
    vertices (Nodes) and Edges. The user interacts with the graph by value
    rather than interacting with the abstraction (this was an issue of some
    concern in the specifications).

Traversable graphs are simple graphs with the additional functionality
    of being "traversable" by depth- and breadth-first search algorithms.
    These algorithms will return the full list of nodes connected to the
    node with the given value by any unbroken chain of edges; this is
    analogous to printing every node of the graph in a list. These functions
    may be modified to perform other duties as they go, if modified.

Weighted graphs are just like traversable graphs, but they have a weighting,
    which is largely useless unless some extra functionality is added.
    Necessary for implementing Djikstra's shortest-path algorithm.

hash_table.py will allow the construction of hash tables of user-defined
    sizes that allow only strings for keys.

    The hashing algorithm used combines bit rotation and XOR hashing, and
        was researched from:
        http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_hashing.aspx

    HashTables will accept any positive integer table size; to optimize
        for performance, the user is expected to determine their own ideal
        hash table size, which is likely to be around 1.6 times the size of
        the anticipated inputs, according to people with evaluation criteria
        I have not yet had time to research.

    HashTable objects may be instantiated by calling:
        HashTable(size)

    HashTable methods include:
        get(key)
            Retrieve from the hash table the value associated with
            the given key string.
        set(key, value)
            Set the value for key in the HashTable to refer to value.
        hash(key)
            Return the hash of a given key string.

Dependencies include Python 2.7

Collaborators:
    Jason Brokaw (binary_heap, priority queue, binary search tree,
        simple graph) ((especially bst deletion))
    Charlie Rode (priority queue, binary search tree)
    Casey MacPhee (binary search tree)

Unit tests were usefully informed by:

    https://github.com/linsomniac/python-unittest-skeleton/
        blob/master/tests/test_skeleton.py

    http://stackoverflow.com/questions/6103825/
        how-to-properly-use-unit-testings-assertraises-with-nonetype-objects

    http://stackoverflow.com/questions/6181555/
        pass-a-unit-test-if-an-exception-isnt-thrown

    https://github.com/charlieRode/data-structures/blob/bst/test_bst.py

Resources used include:https://github.com/BFriedland/data-structures/pull/8

    linked_list:
        http://en.literateprograms.org/Singly_linked_list_%28Python%29

    stack:
        http://en.literateprograms.org/Singly_linked_list_%28Python%29

    validate_parenthetics:
        Own memory

    binary_heap (and priority queue):
        most helpful:
        https://github.com/jbbrokaw/data-structures

        also helpful:
        http://domenicosolazzo.wordpress.com/2010/09/26/
            heapsort-a-python-example/
        http://pravin.paratey.com/posts/binary-heaps-and-priority-queues
        http://en.wikipedia.org/wiki/Binary_heap
        http://interactivepython.org/runestone/static/pythonds/Trees/heap.html

    bst:
        https://github.com/jbbrokaw/data-structures/blob/master/bst.py
        https://github.com/caseymacphee/Data-structures/blob/master/test_bst.py

    hash_table:
        http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_hashing.aspx
        https://github.com/jbbrokaw/data-structures/blob/master/test_hashtable.py

    traversable_graph:
        http://eddmann.com/
            posts/depth-first-search-and-breadth-first-search-in-python/

    weighted_graph:
        Own memory
