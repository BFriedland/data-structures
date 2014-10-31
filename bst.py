
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

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
            self.root_node = Node(val)
            self.size_counter = 1
            self.depth_counter = 1
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

                        current_node.left = Node(val)
                        self.size_counter += 1

                        # Must be incremented upon completion
                        # to reflect the newly added branch:
                        passes_so_far += 1
                        if self.depth_counter < passes_so_far:
                            self.depth_counter = passes_so_far

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

                        current_node.right = Node(val)
                        self.size_counter += 1

                        # Must be incremented upon completion
                        # to reflect the newly added branch:
                        passes_so_far += 1
                        if self.depth_counter < passes_so_far:
                            self.depth_counter = passes_so_far

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

    def contains(self, val):
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
                    return True

                # If it's smaller than the current node,
                # it must go somewhere on the left.
                if current_node.value > val:

                    if val > current_node.left.value:

                        return False

                    else:

                        current_node = current_node.left

                # Then it must be somewhere on the right.
                elif current_node.value < val:

                    if val < current_node.right.value:

                        return False

                    else:

                        current_node = current_node.right

                # Double violation of no-duplication rule
                else:
                    print("Double violation of no-duplication rule discovered")
                    break

    def size(self):
        return self.size_counter

    def depth(self):
        return self.depth_counter

    def balance(self):
        return self.balance_counter




    ## DEBUG
    # Reference:
    # http://stackoverflow.com/questions/5444394/
    #    implementing-binary-search-tree-in-python
    def in_order_print(self, root_of_current_comparison):
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