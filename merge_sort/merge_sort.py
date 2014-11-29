
def merge_sort(the_input):

    # Merge sorting is a 'divide and conquer' algorithm.
    # In this case, 'dividing' involves repeatedly breaking the list into
    # halves until only single elements remain, which are trivially sorted.
    # 'Conquer' is a euphemism for the followup step, wherein all the elements
    # are merged into each other in a way that guarantees the resulting list
    # is sorted.

    # I decided to take the recursive approach once I read the description
    # of how it works, since it separates concerns very cleanly when written.

    # References used:
    # http://en.wikipedia.org/wiki/Merge_sort

    # If the input is a list of only one element or fewer, it is already
    # "sorted" and may be returned immediately. This is the "base case."
    if len(the_input) <= 1:
        return the_input

    # Dividing the list in half:
    halfway_mark = len(the_input) // 2
    left_half = the_input[:halfway_mark]
    right_half = the_input[halfway_mark:]

    # Recursion.
    # This will run the division part over and over again all the way down
    # and then merge all the way up:
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # The tricky part is that at the bottom, the base case will push single
    # elements out of those calls and hand them to this next step:
    return merge_while_sorting(left_half, right_half)


def merge_while_sorting(left_half, right_half):

    # This is the "conquer" part of the algorithm, where split-up elements
    # in the first half are merged back together in order.

    # This variant does not sort in place.
    merged_list = []

    while len(left_half) > 0 or len(right_half) > 0:

        # If both halves still contain unsorted elements...
        if len(left_half) > 0 and len(right_half) > 0:

            # If the first element in the left half is lesser than the
            # first element in the right half...
            if left_half[0] <= right_half[0]:
                # Put it in the merged_list.
                merged_list.append(left_half[0])
                # NOTE! The list must be reassigned to ensure indices don't
                # get mistaken.
                # The list slicer is taking everything in left_half after
                # the zeroeth element -- it's starting at the oneth element
                # and moving onwards.
                left_half = left_half[1:]

            # Else, if the first element in the right half is lesser than
            # the first element in the left half...
            elif right_half[0] < left_half[0]:
                # Put it in the merged_list.
                merged_list.append(right_half[0])
                right_half = right_half[1:]

        # If the left half contains unsorted elements but the right half
        # doesn't...
        elif len(left_half) > 0:
            # Put the first element of the left half into the merged_list.
            merged_list.append(left_half[0])

            # NOTE! The list must be reassigned to ensure indices don't
            # get mistaken.
            left_half = left_half[1:]

        # If the right half contains unsorted elements but the left half
        # doesn't...
        elif len(right_half) > 0:
            # Put the first element of the right half into the merged_list.
            merged_list.append(right_half[0])

            # Remember to reassign the list so indices aren't altered
            # while we're working through it. (That does happen with
            # while loops, doesn't it? Either way, this works safely.)
            right_half = right_half[1:]

    return merged_list


if __name__ == '__main__':

    # "Include an "if __name__ == '__main__':" block at the end of your
    # module that demonstrates the performance characteristics of this
    # sort over a variety of lengths of input in both the best and
    # worst-case scenarios. Executing your module should print informative
    # output about the performance of your sort to the terminal."

    # Sorted is sorted, so I'm going to copy my insertion_sort tests and
    # use the merge_sort algorithm on them.

    import random

    for each_pass in range(0, 100):
        random_list = []
        for each_number in range(0, random.randint(3, 40)):
            random_number = random.randint(0, random.randint(1, 1000))
            random_list.append(random_number)
        print("\n* * * * *\n\nUnsorted:\n    " + str(random_list))
        sorted_random_list = merge_sort(random_list)
        print("Sorted:\n    " + str(sorted_random_list))

        assert len(random_list) == len(sorted_random_list)
        for each_number in range(0, (len(sorted_random_list) - 1)):
            assert (sorted_random_list[each_number]
                    <= sorted_random_list[(each_number + 1)])

    print("\n\n===================\nBegin numeric tests.\n===================")

    dict_of_lists = {
        'list_zero': [0, 0, 0, 0, 0, 0, 0, 0],
        'list_one': [0, 0, 0, 0, 1, 1, 1, 1],
        'list_two': [0, 1, 0, 1, 0, 1, 0, 1],
        'list_three': [0, 1, 1, 0, 1, 1, 0, 0],
        'list_four': [10, 100, 1000000, 10000, 1, 100000, 0, 1000],
        'list_five': [0001, 0010, 0100, 1000, 1100, 0011, 0101, 0110],
    }

    for each_list in dict_of_lists:

        print("\n* * * * *\n\nUnsorted:\n    " + str(dict_of_lists[each_list]))
        sorted_list = merge_sort(dict_of_lists[each_list])
        print("Sorted:\n    " + str(sorted_list))

    print("\nPerformance is O(nlogn) in the best, worst, and typical cases."
          "\nIt's very predictable that way.")

    raw_input("\n    Press enter to begin the BONUS ROUND!")

    strings_dict = {
        'list_six': "Not the most useful application for sorting.",
        'list_seven': "badcfehgjilknmporqtsvuxwzy",
        'list_eight': "list_seven is not as random as it may appear",
        'list_nine': "the quick brown fox jumps over the lazy dog",
    }

    def sort_string(input_string):
        sorting_list = []
        for each_character in input_string:
            sorting_list.append(ord(each_character))
        sorting_list = merge_sort(sorting_list)
        return_list = []
        for each_number in sorting_list:
            return_list.append(chr(each_number))
        return [''.join(return_list)][0]

    for each_list in strings_dict:
        print("\n* * * * *\n\nUnsorted:\n    " + str(strings_dict[each_list]))
        sorted_list = sort_string(strings_dict[each_list])
        print("Sorted:\n    " + str(sorted_list))

    print
