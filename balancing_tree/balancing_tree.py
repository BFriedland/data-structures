
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        # Needed for deletion, to heal our poor tree's severed stumps
        self.parent = None

        # For AVL tree-balancing, a node must
        # keep track of its own balance offset.
        # Note that the root node always starts
        # with a balance_offset of zero.
        self.balance_offset = 0

    def __str__(self):
        # inspired by:
        # https://github.com/caseymacphee/Data-structures/blob/master/bst.py
        return str(self.value)


class BalancingBinarySearchTree:

    # With much assistance from:
    # https://github.com/caseymacphee/Data-structures/blob/master/bst.py
    # and
    # http://stackoverflow.com/questions/5444394/
    #    implementing-binary-search-tree-in-python

    def __init__(self):
        self.root_node = None
        self.size_counter = 0

        # This is not related to the AVL tree's balance measures, but
        # it can serve as a mildly interesting way to keep track of the
        # performance balance of the tree balancing function by comparison.
        self.size_balance_counter = 0

    def correct_balance(self, this_node):

        # Reference:
        # http://interactivepython.org/
        #     courselib/static/pythonds/Trees/balanced.html

        if ((this_node.balance_offset > 1)
           or (this_node.balance_offset < -1)):

            self.avl_balance(this_node)

            # It shouldn't need to continue checking after this point, sp:
            return

        if this_node.parent is not None:

            # Check if this_node is the left branch of the parent node:
            if this_node.parent.left == this_node:

                # Balance offsets on each node match the direction of the
                # tree's sign -- left is positive offset, right is negative.
                this_node.parent.balance_offset += 1

            # Now check if this_node is the right branch of the parent node:
            elif this_node.parent.right == this_node:
                this_node.parent.balance_offset -= 1

            # If the parent node's balance is not zero, check them too.
            # ((Note that this whole procedure only works properly if
            # correct_balance() is called after every change to the tree;
            # when this cannot be guaranteed, there may be situations
            # where the tree doesn't realize the balance is askew.))
            if this_node.parent.balance_offset != 0:

                # Note: This is a tail recursion point. It is NOT intended
                # to be the same as calling self.avl_balance().
                self.correct_balance(this_node.parent)

    def avl_balance(self, this_node):

        # Reference:
        # http://interactivepython.org/
        #     courselib/static/pythonds/Trees/balanced.html

        # If this_node's balance_offset is zero, no rebalancing is needed.
        if this_node.balance_offset == 0:
            return

        # If the node's balance offset is negative,
        # the branches below it must be right-heavy.
        if this_node.balance_offset < 0:

            # Being right-heavy doesn't mean that the right branch is
            # correctly balanced, itself. The right branch could still
            # be locally imbalanced to the left. In this case a separate
            # pre-balancing step on the right branch should be performed
            # before self.rotate_left(this_node) is called.
            if this_node.right.balance_offset > 0:
                self.rotate_right(this_node.right)
                # Once the subtree's rotation is corrected, this_node may
                # safely be rotated to the left:
                self.rotate_left(this_node)
            # If there is no imbalance in the subtree opposite to the
            # imbalance of this_node, this_node may safely be rotated left:
            else:
                self.rotate_left(this_node)

        # Handling cases where the tree is left-heavy:
        elif this_node.balance_offset > 0:

            # As above, but with inverted balance checking.
            # If this_node's left branch has a rightwards imbalance
            # (even though this_node is itself imbalanced leftwards)...
            if this_node.left.balance_offset < 0:

                # ... then pre-balance the left branch leftwards to correct
                # that rightwards imbalance...
                self.rotate_left(this_node.left)
                # ... and then rotate this_node to resolve its own imbalance:
                self.rotate_right(this_node)

            # If this_node's left branch has no rightwards imbalance of
            # its own, this_node may safely be rotated rightwards
            # (to correct its own leftwards offset).
            else:
                self.rotate_right(this_node)

    def rotate_left(self, old_root_node):

        # old_root_node refers to the node that is being rotated;
        # its position (relative to the rest of the tree) is where one
        # of its branch nodes will be after we're done.
        # The term "root" will refer to that relative position.

        # Before swapping any nodes' branch or parent references,
        # assign the right branch of the old_root_node to a holding
        # variable so we can keep track of it.
        new_root_node = old_root_node.right

        # The first node pointer swap.
        # (This effectively replaces the old_root_node's right pointer
        # with the previous occupant's own left pointer, leaving new_root_node
        # with a reference to the old_root_node as a parent, but without
        # a corresponding branch reference on old_root_node.)
        old_root_node.right = new_root_node.left

        # Before moving on, we must tie up a loose end we created --
        # the new_root_node.left pointer is changed, but its parent reference
        # is now incorrect. So, if there is actually a node there (see None),
        # make it aware of the change in parentage:
        if new_root_node.left is not None:
            new_root_node.left.parent = old_root_node

        # This informs the new_root_node of its parent node, by way of
        # the parent reference on the old_root_node. This is where
        # I started to think of the "old_root_node" as being the
        # "old_root_node" due to how many pointers have now been swapped.
        new_root_node.parent = old_root_node.parent

        # If the old_root_node was the root of
        # the tree, two special changes must be made.
        # If a node doesn't have a parent node, it had
        # better be the root of the tree. You can also
        # check if old_root_node == self.root_node
        # if you'd rather the relation be more explicit.
        if old_root_node.parent is None:

            # First, swap the tree's root reference:
            self.root_node = new_root_node

        # If the old_root_node was not the root of the tree, we can
        # now inform the parents of their horizontal transdoption:
        else:

            # Check if the old_root_node was the left child of its parent.
            if old_root_node.parent.left == old_root_node:

                # If so, correct the old parent's left branch pointer to
                # the new_root_node, cementing its position in the tree:
                old_root_node.parent.left = new_root_node

            # If the old_root_node wasn't the tree root and it wasn't
            # the left branch of its parent node, it must have been the
            # right branch of its parent node.
            else:

                # Informing the root position's parent of the new root node:
                old_root_node.parent.right = new_root_node

        # Now that the nodes have been swapped in each others' pointers
        # and the parent node has been informed, we can move the
        # old_root_node in to the open slot left by reassigning
        # new_root.left.parent to old_root_node.left (or rather,
        # assigning the nodes in *that position* to *that position*.)
        new_root_node.left = old_root_node

        # Swap the old_root_node's parent
        # pointer to the new_root_node.
        old_root_node.parent = new_root_node

        # Next we must properly modify all involved nodes'
        # balance_offsets to reflect the recent changes.
        # Note that this alteration is NOT
        # handled by correct_balance().

        # First, increment the old_root_node's balance offset by one to
        # reflect its leftward shift:
        old_root_node.balance_offset += 1

        # Then, if the new_root_node's balance_offset is negative (rightwards),
        # apply it to the old_root_node's balance_offset as an increment.
        # This is like taking the absolute value of the new_root_node's
        # balance_offset and adding it to the old_root_node's balance_offset,
        # but only if it is a value below zero before absolute-valuification.
        # Figuring this step out had me boggled for a while and would
        # probably require some extra research to really memorize.
        # A full algebraic derivation of this logic can be found at:
        # http://interactivepython.org/
        #     courselib/static/pythonds/Trees/balanced.html
        old_root_node.balance_offset -= min(new_root_node.balance_offset, 0)

        # Next is the corresponding procedure in the opposite direction
        # for the new_root_node's balance_offset.
        new_root_node.balance_offset += 1

        # Remember we're rotating left here, so everything should only go up.
        new_root_node.balance_offset += max(old_root_node.balance_offset, 0)

        # And we're done with left-rotating! Hooray!

    def rotate_right(self, old_root_node):

        # Once again, thanks to
        # http://interactivepython.org/
        #     courselib/static/pythonds/Trees/balanced.html
        # for the excellent reference.

        # Rotating right is just like rotating left, except in
        # the opposite direction;
        # i.e., it's the symmetrical counterpart to rotate_left().
        # For this reason, I'll omit most of the comments I made in
        # rotate_left() and instead point out the relevant differences.
        # "Root" herein refers to the relative position of the root node
        # of the subtree that is being rotated. It does NOT refer to the
        # entire tree's root_node.

        # Since we're rotating right, we'll need to use the old_root_node's
        # left branch as the new_root_node.
        new_root_node = old_root_node.left

        old_root_node.left = new_root_node.right

        if new_root_node.right is not None:
            new_root_node.right.parent = old_root_node

        # Note that the symmetric changes only apply to chiral distinctions.
        new_root_node.parent = old_root_node.parent

        if old_root_node.parent is None:

            self.root_node = new_root_node

        else:

            if old_root_node.parent.right == old_root_node:

                old_root_node.parent.right = new_root_node

            else:

                old_root_node.parent.left = new_root_node

        new_root_node.right = old_root_node

        old_root_node.parent = new_root_node

        # This next part is critically distinct from
        # its counterpart in left_rotation().

        # Where left_rotation was always incrementing offsets, right_rotation
        # will only ever be decrementing them.

        # This means we must swap the 'crement operator's sign to negative:
        old_root_node.balance_offset -= 1

        # In rotate_left() it was necessary to decrement by the least of
        # either a potentially negative number or zero -- an operation
        # which only ever yielded a HIGHER value or kept the number the same.
        # This is because subtracting by a negative number causes the resulting
        # value to increase, where adding a negative number to something
        # causes it to decrease. Third grade stuff, maybe, but all
        # too easily mistaken if not laid out explicitly.
        old_root_node.balance_offset -= max(new_root_node.balance_offset, 0)

        new_root_node.balance_offset -= 1

        # Here, instead of adding the greatest one of either a potentially
        # positive number or zero (as in leftward rotation), we will be
        # "adding" the least one of a potentially negative number or zero,
        # (making the number either decrease in value or stay the same).
        new_root_node.balance_offset += min(old_root_node.balance_offset, 0)

        # Once again, a full derivation of left_rotate()'s version
        # of the above balance_offset modification may be found at
        # the same site I referenced while doing this assignment:
        # http://interactivepython.org/
        #     courselib/static/pythonds/Trees/balanced.html

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
            self.root_node = Node(val)
            self.size_counter = 1
            # The center node has balance zero, by definition:
            self.size_balance_counter = 0

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

                        current_node.left = Node(val)
                        current_node.left.parent = current_node
                        self.size_counter += 1


                        # This information is related to the first branchpoint;
                        # it cannot be determined from the mere fact we are
                        # placing a node which is on the left of *something*.
                        if which_side_are_we_placing_it_on == "Left":
                            self.size_balance_counter += 1

                        # If a node was added here, check for
                        # and correct potential tree imbalances:
                        self.correct_balance(current_node.left)

                    else:

                        # passes_so_far updates at the top of the loop.
                        # It doesn't need to be touched here.
                        current_node = current_node.left

                # Then it's closer to the median value of the tree.
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

                        current_node.right = Node(val)
                        current_node.right.parent = current_node
                        self.size_counter += 1

                        # This information is related to the first branchpoint;
                        # it cannot be determined from the mere fact we are
                        # placing a node which is on the right of *something*.
                        if which_side_are_we_placing_it_on == "Right":
                            self.size_balance_counter -= 1

                        # If a node was added here, check for
                        # and correct potential tree imbalances:
                        self.correct_balance(current_node.right)

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

                    if current_node.left is not None:

                        current_node = current_node.left

                    # Since we start at the root, False is safe here.
                    # In fact, it's required to prevent infinilooping.
                    else:
                        return False

                # Then it must be somewhere on the right.
                elif current_node.value < val:

                    if current_node.right is not None:

                        current_node = current_node.right

                    else:
                        return False


                elif (not current_node.left) and (not current_node.right):

                    return False

                # Double violation of no-duplication rule
                else:
                    print("Double violation of no-duplication rule discovered")
                    break

    def size(self):
        return self.size_counter

    def depth(self):
        return self._return_tree_max_depth()

    def balance(self):
        # Deprecated in favor of a recursive solution:
        # return self.size_balance_counter
        # Deprecated because size balance is unimportant for BSTs:
        # return self._return_tree_size_balance(self.root_node)
        # This returns the HEIGHT balance of the BST:
        return self.root_node.balance_offset

    def _return_tree_size_balance(self, current_node, is_first_pass=True):

        # This returns SIZE imbalance for a node's subtrees.
        # Size imbalances are totally unimportant for lookup times in
        # a binary search tree, because comparisons only happen at
        # branching points.
        # So, this code is largely unimportant and is only a novelty now.

        # Note that this function is recursive in three locations, but
        # only ever calls recursion at most twice from each previous call.
        # It makes zero recursive calls on nodes with no branches.

        # The root_node has zero effect on balance, but every other node
        # will change the balance counter by one each.
        return_value = 0

        # This is the result of my discovering AVL trees only balance
        # subtrees by HEIGHT, not SIZE. The exception is only raised
        # if AVL is not working properly -- the balance_offset tracks
        # HEIGHT BALANCE of subtrees, not SIZE BALANCE, which is tracked
        # by self._return_tree_size_balance(), which is totally unimportant
        # for the purposes of speeding up information retrieval.
        if current_node.balance_offset > 1:
            raise Exception("  HEIGHT IMBALANCE! {}".format(
                current_node.balance_offset))

        if is_first_pass is False:
            return_value += 1

        if current_node.left:
            return_value += self._return_tree_size_balance(
                current_node.left, is_first_pass=False)

            # Leaving in the following few lines for future reference:
            # if is_first_pass == True:
            #     leftside = self._return_tree_size_balance(
            #         current_node.left, is_first_pass=False)

            #     print("Leftside: {}".format(leftside))
            #     print("Leftside in-order print:")
            #     self.in_order_print(current_node.left)

        # Only the top of the recursion tree should flip the sign of the
        # size of the right portion of the tree (to negative).
        if is_first_pass is True:
            if current_node.right:

                return_value -= self._return_tree_size_balance(
                    current_node.right, is_first_pass=False)

                # Leaving in the following few lines for future reference:
                # rightside = self._return_tree_size_balance(
                #     current_node.right, is_first_pass=False)
                # print("Rightside: -{}".format(rightside))
                # print("Rightside in-order print:")
                # self.in_order_print(current_node.right)

        elif is_first_pass is False:
            if current_node.right:
                return_value += self._return_tree_size_balance(
                    current_node.right, is_first_pass=False)

        return return_value

    def delete(self, val, current_node=None):

        # This function handles both delete-by-object and delete-by-value.
        # Note that a Node containing another Node will fail this check,
        # but then, that shouldn't ever happen. Caveat... usor?
        if isinstance(current_node, Node):
            the_node_to_delete = current_node
        else:
            the_node_to_delete = self.contains(val, return_the_node=True)

        # contains(val, return_the_node=True) will return False if there
        # is no node with that value in the tree.
        if the_node_to_delete is False:
            # Then the node is not in the tree.
            # "Fail" gracefully:
            return None

        elif isinstance(the_node_to_delete, Node):

            # If it gets past that check, we know it's in the tree because
            # self.contains() actually returned a node from the tree.
            # So, do balance ahead of time:
            if the_node_to_delete.value == self.root_node.value:
                # Then it's the root node.
                # Still needs to be fully considered for deletion,
                # so we can't end the function when we know this.
                self.size_balance_counter += 0  # Syntactic consistency
            elif the_node_to_delete.value > self.root_node.value:
                # Righter trees are more negative,
                # lefter trees are more positive.
                self.size_balance_counter += 1
            elif the_node_to_delete.value < self.root_node.value:
                self.size_balance_counter -= 1

            # If the node is a "leaf" (ie, it has no descendants),
            # delete it outright.
            if ((the_node_to_delete.left is None)
               and (the_node_to_delete.right is None)):

                # The root_node case:
                if the_node_to_delete.parent is not None:

                    if the_node_to_delete.parent.right == the_node_to_delete:
                        the_node_to_delete.parent.right = None

                    if the_node_to_delete.parent.left == the_node_to_delete:
                        the_node_to_delete.parent.left = None

                else:
                    # Inform the tree it has no root_node anymore.
                    self.root_node = None

                # Do we even need to do this if we remove the references?
                # Yes, since extra-arboreal objects might still contain
                # references to this node.
                # AVL trees do not need to rebalance for
                # height when a leaf has been deleted.
                del the_node_to_delete
                return None

            # If the node is a branch with one descendant,
            # mend the tree by connecting that descendant to
            # the node's parent.
            elif ((the_node_to_delete.right is not None)
                  and (the_node_to_delete.left is None)):

                if the_node_to_delete.parent is not None:

                    the_node_to_delete.parent.right = the_node_to_delete.right
                    the_node_to_delete.right.parent = the_node_to_delete.parent

                    # AVL-balanced trees must rebalance at every node deletion:
                    self.correct_balance(the_node_to_delete.parent)

                else:
                    # Inform the tree the root_node has changed:
                    self.root_node = the_node_to_delete.right
                    self.correct_balance(self.root_node)

                del the_node_to_delete

            elif ((the_node_to_delete.right is None)
                  and (the_node_to_delete.left is not None)):

                if the_node_to_delete.parent is not None:

                    the_node_to_delete.parent.left = the_node_to_delete.left
                    the_node_to_delete.left.parent = the_node_to_delete.parent

                    # AVL-balanced trees must rebalance at every node deletion:
                    self.correct_balance(the_node_to_delete.parent)

                else:
                    # Inform the tree the root_node has changed:
                    self.root_node = the_node_to_delete.left
                    self.correct_balance(self.root_node)

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

                    current_depth += 1
                    # Which way at top is opposite the way
                    # we're looking down the subtree.
                    if which_way_at_top == "Left":
                        if each_node.right is not None:
                            return _find_furthest_subtree_size_and_node(
                                each_node.right, "Left", current_depth)
                        else:
                            return current_depth, each_node
                    else:
                        if each_node.left is not None:
                            return _find_furthest_subtree_size_and_node(
                                each_node.left, "Right", current_depth)
                        else:
                            return current_depth, each_node

                left_subtree_size, rightest_left_subtree_node \
                    = _find_furthest_subtree_size_and_node(
                        the_node_to_delete.left, "Left")
                right_subtree_size, leftest_right_subtree_node \
                    = _find_furthest_subtree_size_and_node(
                        the_node_to_delete.right, "Right")

                # # Hackishly force one to be bigger if they're equal.
                # # Makes it balance by height, since it's an AVL tree.
                # if left_subtree_size == right_subtree_size:
                #     # Add it to the right subtree
                #     # because negative balance is righter.
                #     right_subtree_size += (self.root_node.balance_offset /
                #                            abs(self.root_node.balance_offset))

                if left_subtree_size >= right_subtree_size:
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

            # I realized it's not possible to quickly tell if there's
            # another node with the same depth on some other branch
            # when trying to find depth via state held in a Node attribute.
            # So I made a recursive solution that adds the depth
            # of every node to a list held by the tree and finds
            # the max value in that list, and removed Nodes' "depth" attribute.

            return None

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
            if root_of_current_comparison is None:
                # This is a tree-level list so that
                # many recursive branches can all add to it.
                # I'm virtually certain this is not ideal,
                # but I also think it'll work!
                self._depth_finder_list.append(depth_at_this_step)
                return
            # Increment this AFTER we determine if there was a node here
            # or not, since we append this value to the list BEFORE this.
            depth_at_this_step += 1

            _recursive_depth_list_builder(root_of_current_comparison.left,
                                               depth_at_this_step=depth_at_this_step)
            _recursive_depth_list_builder(root_of_current_comparison.right,
                                               depth_at_this_step=depth_at_this_step)

        _recursive_depth_list_builder(self.root_node)

        # If it didn't return any list contents, it
        # should return a depth of zero, since that's
        # how it got that problem in the first place.
        if len(self._depth_finder_list) == 0:
            return 0
        else:
            return max(self._depth_finder_list)

    # Reference:
    # http://stackoverflow.com/questions/5444394/
    #    implementing-binary-search-tree-in-python

    # Is a public function, so no underscore.
    def in_order_print(self, root_of_current_comparison='self.root', returning=False):
        ''' Print the entire tree in ascending order of value.
        This function is always called with a Node from the tree
        it's called on. To print the whole tree, call:
        self.in_order_print(self.root_node)
        To return values in a list instead of printing them
        individually, use the kwarg returning=True '''

        if root_of_current_comparison == 'self.root_node':
            root_of_current_comparison = self.root_node

        if not root_of_current_comparison:
            return []

        return_list = []

        return_list += self.in_order_print(root_of_current_comparison.left, returning=True)
        return_list += [root_of_current_comparison.value]
        return_list += self.in_order_print(root_of_current_comparison.right, returning=True)

        if returning is True:
            return return_list

        if returning is False:
            print return_list


if __name__ == "__main__":

    balancing_tree = BalancingBinarySearchTree()

    print("The worst case scenario to find 9 in an unbalanced tree\n"
          "would be as long as a linked list, or O(n).\n\nHowever, for "
          "an AVL tree, it is merely O(log n), because\nthe tree balances "
          "by height as necessary at every insertion.\nThe depth of this "
          "worst-case tree is therefore only four when\nit could have "
          "been nine, and its height balance offset is,\ncorrectly, "
          "fewer than two points from zero:")

    for each in range(1, 10):
        balancing_tree.insert(each)
    balancing_tree.in_order_print(balancing_tree.root_node)
    print("Size: %r\nDepth: %r\nBalance:%r\n" % (balancing_tree.size(),
                                                 balancing_tree.depth(),
                                                 balancing_tree.balance()))

    balancing_tree = BalancingBinarySearchTree()
    print("Best case scenario to find 9 is constant time:")
    balancing_tree.insert(9)
    balancing_tree.in_order_print(balancing_tree.root_node)
    print("Size: %r\nDepth: %r\nBalance:%r\n" % (balancing_tree.size(),
                                                 balancing_tree.depth(),
                                                 balancing_tree.balance()))

    print("Due to unremitting balancing at every insertion, the average\n"
          "case lookup operation on *all* AVL-sorted BSTs is O(log n).\n")

    proceed = raw_input("The algorithm will next print the contents and\n"
                        "metrics of one hundred randomly generated trees.\n"
                        "If this is not desired, press control-c.\n> ")

    import random

    print("\n================= Begin random tree examples =================\n")

    for each_pass in range(0, 100):
        balancing_tree = BalancingBinarySearchTree()
        for each in range(5, random.randint(10, 100)):
            balancing_tree.insert(random.randint(0, 100))
        balancing_tree.in_order_print(balancing_tree.root_node)
        print("Size: %r\nDepth: %r\nBalance:%r\n" % (balancing_tree.size(),
                                                     balancing_tree.depth(),
                                                     balancing_tree.balance()))
