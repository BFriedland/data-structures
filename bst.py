
class Node:

    def __init__(self, val, depth):
        self.value = val
        self.left = None
        self.right = None
        # Needed for deletion, to heal our poor tree's severed stumps
        self.parent = None
        # Needed for deletion to make updating depth easier
        self.depth_of_node = depth

    def __str__(self):
        # inspired by:
        # https://github.com/caseymacphee/Data-structures/blob/master/bst.py
        return str(self.value)


class BinarySearchTree:

    # With much assistance from:
    # https://github.com/caseymacphee/Data-structures/blob/master/bst.py
    # and
    # http://stackoverflow.com/questions/5444394/
    #    implementing-binary-search-tree-in-python

    def __init__(self):
        self.root_node = None
        self.size_counter = 0
        self.depth_counter = 0
        self.balance_counter = 0

    def insert(self, val):
        ''' Insert val into the binary search tree as a node, maintaining
        order. If val is already present, it will be ignored. '''

        if val is None:
            raise TypeError("NoneType is not sortable")

        if not isinstance(val, int):
            raise TypeError("May only insert integers")

        # If there's no root node, make this node the root node.
        # It's a bit like a reset button, and it's more reliable to
        # verify these things here in the event of an imaginary
        # horizontal attack on tree integrity.
        if self.root_node is None:
            self.depth_counter = 1
            self.root_node = Node(val, depth=1)
            self.size_counter = 1
            # The center node has balance zero, by definition:
            self.balance_counter = 0

        else:

            current_node = self.root_node
            passes_so_far = 0
            which_side_are_we_placing_it_on = "Unknown"

            # Break after node creation or upon duplication discovery.
            while True:

                # This will only be incremented when the tree moves
                # down a rank, and since it resets to zero every insertion,
                # this reflects the depth of the tree.
                passes_so_far += 1

                # No-duplication rule:
                if current_node.value == val:
                    break

                # If it's smaller than the current node,
                # it must go somewhere on the left.
                if current_node.value > val:

                    # Only updates on the first branchpoint.
                    if which_side_are_we_placing_it_on == "Unknown":
                        which_side_are_we_placing_it_on = "Left"

                    if current_node.left is None:

                        # Must be incremented upon completion
                        # to reflect the newly added branch.
                        # Above the new Node construction
                        # because it is used by it.
                        passes_so_far += 1
                        if self.depth_counter < passes_so_far:
                            self.depth_counter = passes_so_far

                        current_node.left = Node(val, depth=passes_so_far)
                        current_node.left.parent = current_node
                        self.size_counter += 1


                        # This information is related to the first branchpoint;
                        # it cannot be determined from the mere fact we are
                        # placing a node which is on the left of *something*.
                        if which_side_are_we_placing_it_on == "Left":
                            self.balance_counter += 1
                    else:

                        # passes_so_far updates at the top of the loop.
                        # It doesn't need to be touched here.
                        current_node = current_node.left

                # Then it's closer to the media value of the tree.
                # This is not like the binary heap; the middlemost
                # value is at the root.
                elif current_node.value < val:

                    # Only updates on the first branchpoint.
                    if which_side_are_we_placing_it_on == "Unknown":
                        which_side_are_we_placing_it_on = "Right"

                    if current_node.right is None:

                        # Must be incremented upon completion
                        # to reflect the newly added branch.
                        # Above the new Node construction
                        # because it is used by it.
                        passes_so_far += 1
                        if self.depth_counter < passes_so_far:
                            self.depth_counter = passes_so_far

                        current_node.right = Node(val, depth=passes_so_far)
                        current_node.right.parent = current_node
                        self.size_counter += 1


                        # This information is related to the first branchpoint;
                        # it cannot be determined from the mere fact we are
                        # placing a node which is on the right of *something*.
                        if which_side_are_we_placing_it_on == "Right":
                            self.balance_counter -= 1

                    else:

                        # passes_so_far updates at the top of the loop.
                        # It doesn't need to be touched here.
                        current_node = current_node.right

                # If the node is precisely equal, it violates the
                # no-duplication rule. It should never get here, but
                # just in case I'm not as smart as I think I am...
                else:
                    print("Double violation of no-duplication rule discovered")
                    break

    def contains(self, val, return_the_node=False):
        ''' Return True is val is in the binary search tree;
        otherwise, return False. '''

        if val is None:
            raise ValueError("NoneType is not sortable")

        # If there's no root node, make this node the root node.
        if self.root_node is None:
            return False

        else:

            current_node = self.root_node

            # Break after node creation or upon duplication discovery.
            while True:

                # No-duplication rule:
                if current_node.value == val:

                    if return_the_node is True:
                        # NOTE: if there is no such node,
                        # the return is still False.
                        return current_node

                    else:

                        return True

                # If it's smaller than the current node,
                # it must go somewhere on the left.
                if current_node.value > val:

                    if current_node.left:

                        if val > current_node.left.value:

                            return False

                        else:

                            current_node = current_node.left

                # Then it must be somewhere on the right.
                elif current_node.value < val:

                    if current_node.right:

                        if val < current_node.right.value:

                            return False

                        else:

                            current_node = current_node.right

                elif (not current_node.left) and (not current_node.right):

                    return False

                # Double violation of no-duplication rule
                else:
                    print("Double violation of no-duplication rule discovered")
                    break

    def size(self):
        return self.size_counter

    def depth(self):
        return self.depth_counter
        # could probably also call:
        # return self._return_tree_max_depth()

    def balance(self):
        return self.balance_counter

    def delete(self, val, current_node=None):

        if isinstance(current_node, Node):
            the_node_to_delete = current_node
        else:
            the_node_to_delete = self.contains(val, return_the_node=True)

        # contains(val, return_the_node=True) will return False if there
        # is no node with that value in the tree.
        if the_node_to_delete is False:
            # Then the node is not in the tree.
            # "Fail" gracefully:
            return

        elif isinstance(the_node_to_delete, Node):

            # If it gets past that check, we know it's in the tree because
            # self.contains() actually returned a node from the tree.
            # So, do balance ahead of time:
            if the_node_to_delete.value == self.root_node.value:
                # Then it's the root node.
                # Still needs to be fully considered for deletion,
                # so we can't end the function when we know this.
                self.balance_counter += 0  # Syntactic consistency
            elif the_node_to_delete.value > self.root_node.value:
                # Righter trees are more negative,
                # lefter trees are more positive.
                self.balance_counter += 1
            elif the_node_to_delete.value < self.root_node.value:
                self.balance_counter -= 1

            # If the node is a "leaf" (ie, it has no descendants),
            # delete it outright.
            if ((the_node_to_delete.left is None)
               and (the_node_to_delete.right is None)):

                if the_node_to_delete.parent.right == the_node_to_delete:
                    the_node_to_delete.parent.right = None

                if the_node_to_delete.parent.left == the_node_to_delete:
                    the_node_to_delete.parent.left = None

                # Do we even need to do this if we remove the references?
                # Yes, since extra-arboreal objects might still contain
                # references to this node.
                del the_node_to_delete
                return

            # If the node is a branch with one descendant,
            # mend the tree by connecting that descendant to
            # the node's parent.
            elif ((the_node_to_delete.right is not None)
                  and (the_node_to_delete.left is None)):

                the_node_to_delete.parent.right = the_node_to_delete.right
                the_node_to_delete.right.parent = the_node_to_delete.parent

                del the_node_to_delete

            elif ((the_node_to_delete.right is None)
                  and (the_node_to_delete.left is not None)):

                the_node_to_delete.parent.left = the_node_to_delete.left
                the_node_to_delete.left.parent = the_node_to_delete.parent

                del the_node_to_delete

            # If the node is a branch with two descendants,
            # mend the tree in a way that brings it closer
            # to a well-balanced state (self.balance == 0)
            elif ((the_node_to_delete.right is not None)
                  and (the_node_to_delete.left is not None)):

                # This function returns the length of a given node's subtree.
                # It is to be called on the_node_to_delete.left AND
                # the_node_to_delete.right, and whichever returns greater will
                # be the new replacement node.
                # If tied, which_way_to_balance_the_whole_tree will decide it.
                def _find_furthest_subtree_size_and_node(
                        each_node, which_way_at_top, current_depth=1):

                    if each_node is None:
                        return current_depth, each_node.parent
                    else:
                        current_depth += 1
                        # Which way at top is opposite the way
                        # we're looking down the subtree.
                        if which_way_at_top == "Left":
                            return _find_furthest_subtree_size_and_node(
                                each_node.right, "Left", current_depth)
                        else:
                            return _find_furthest_subtree_size_and_node(
                                each_node.left, "Right", current_depth)

                left_subtree_size, rightest_left_subtree_node \
                    = _find_furthest_subtree_size_and_node(
                        self.the_node_to_delete.left, "Left")
                right_subtree_size, leftest_right_subtreenode \
                    = _find_furthest_subtree_size_and_node(
                        self.the_node_to_delete.right, "Right")

                # Hackishly force one to be bigger if they're equal.
                # Makes it balance closer to the root.
                if left_subtree_size == right_subtree_size:
                    # Add it to the right subtree
                    # because negative balance is righter.
                    right_subtree_size += (self.balance / abs(self.balance))

                if left_subtree_size > right_subtree_size:
                    # Then rebalance the tree using the left
                    # subtree as the new replacement node.

                    the_node_to_delete.value = rightest_left_subtree_node.value
                    # We must run delete() on the rightest left subtree
                    # node because it could still have a left branch on it.
                    self.delete(rightest_left_subtree_node)

                elif left_subtree_size < right_subtree_size:
                    # Then rebalance the tree using the right
                    # subtree as the new replacement node.

                    the_node_to_delete.value = leftest_right_subtree_node.value
                    # We must run delete() on the rightest left subtree
                    # node because it could still have a left branch on it.
                    self.delete(leftest_right_subtree_node)

            # I realized it's not possible to tell if there's
            # another node with the same depth on some other branch
            # when trying to find depth via the Node attribute.
            # So I made a recursive solution that adds the depth
            # of every node to a list held by the tree and finds
            # the max value in that list.
            # Call it once after node deletion:
            self.depth = self._return_tree_max_depth()
            # Note: this only matters if self.depth is an attribute.
            # Leaving it in for demonstration purposes since that code
            # already works.

        else:
            raise TypeError("%s returned by contains but is not Node type"
                            % (the_node_to_delete))

    def _return_tree_max_depth(self):
        # Reset the old list.
        # This list is kept in the tree object because
        # we need lots of little threads to add to it
        # while they're branching out from each other.
        # I think having them all return things would
        # cause return problems or something -- I could
        # append the result of each thing to a list and
        # send the list up, but this is easier to debug...
        self._depth_finder_list = []

        # Init it to zero, since we always start "above" the root node.
        def _recursive_depth_list_builder(root_of_current_comparison,
                                          depth_at_this_step=0):
            if not root_of_current_comparison:
                # This is a tree-level list so that
                # many recursive branches can all add to it.
                # I'm virtually certain this is not ideal,
                # but I also think it'll work!
                self._depth_finder_list.append(depth_at_this_step)
                return
            # Increment this AFTER we determine if there was a node here
            # or not, since we append this value to the list BEFORE this.
            depth_at_this_step += 1

            # ... also, cover up any mistakes delete() might have made...
            # Nothing to see here, move along...
            if root_of_current_comparison.depth != depth_at_this_step:
                root_of_current_comparison.depth = depth_at_this_step
            self._recursive_depth_list_builder(root_of_current_comparison.left,
                                               depth_at_this_step=depth_at_this_step)
            self._recursive_depth_list_builder(root_of_current_comparison.right,
                                               depth_at_this_step=depth_at_this_step)
            _recursive_depth_list_builder(self.root_node)

        # If it didn't return any list contents, it
        # should return a depth of zero, since that's
        # how it got that problem in the first place.
        if len(self._depth_finder_list) == 0:
            return 0
        else:
            return max(self._depth_finder_list)


    ## DEBUG
    # Reference:
    # http://stackoverflow.com/questions/5444394/
    #    implementing-binary-search-tree-in-python

    # Is a public function, so no underscore.
    def in_order_print(self, root_of_current_comparison):
        ''' Print the entire tree in ascending order of value.
        This function is always called with a Node from the tree
        it's called on. To print the whole tree, call:
        self.in_order_print(self.root_node) '''
        if not root_of_current_comparison:
            return
        self.in_order_print(root_of_current_comparison.left)
        print(root_of_current_comparison.value)
        self.in_order_print(root_of_current_comparison.right)

    ## / DEBUG


if __name__ == "__main__":

    bst = BinarySearchTree()
    print("Worst case scenario to find 9 is as long as a linked list, or O(n):")
    for each in range(1, 10):
        bst.insert(each)
    bst.in_order_print(bst.root_node)
    print("Size: %r\nDepth: %r\nBalance:%r\n" % (bst.size(), bst.depth(), bst.balance()))

    bst = BinarySearchTree()
    print("Best case scenario to find 9 is constant time, when it's placed at the top:")
    bst.insert(9)
    bst.in_order_print(bst.root_node)
    print("Size: %r\nDepth: %r\nBalance:%r\n" % (bst.size(), bst.depth(), bst.balance()))

    print("The average case is O(log n).\n")