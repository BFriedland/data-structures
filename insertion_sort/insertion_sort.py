
# Inspired by/learned from:
# http://en.wikipedia.org/wiki/Insertion_sort
# http://www.geekviewpoint.com/python/sorting/insertionsort


def insertion_sort(the_list):

    # Iteration must range over indices because we need to refer to
    # numbers' positions in the list in order to insert properly.
    for each_number_index in range(1, len(the_list)):

        # First, extract the number we're sorting.
        number_to_be_reinserted = the_list[each_number_index]

        # The index we'll start comparing that number against is
        # should be equal to or lesser than the index from which
        # we extracted the number, since we're going to check numbers
        # in order of decreasing index value.
        # This will have the net effect of ordering the list from
        # zeroeth index to final index according to the direction of the
        # second comparison operator used inside the while loop below.
        current_index_to_compare_against = each_number_index

        # While we're not yet at the last slot in the list and the
        # number we're moving around to reinsert is less than the value
        # of the number one index to the left of the index we're
        # currently looking at ...
        while ((current_index_to_compare_against > 0)
                and (number_to_be_reinserted
                     < the_list[(current_index_to_compare_against - 1)])):
            # ... if the number we're inserting is not bigger than the number
            # one slot to the left of the current index, make the current
            # number equal to the number one slot to the left ...
            the_list[current_index_to_compare_against] \
                = the_list[(current_index_to_compare_against - 1)]

            # ... and decrement the index we're comparing against.
            current_index_to_compare_against -= 1

        # If the number we're currently attempting to reinsert into the
        # list is not less than the number one slot to the left of whatever
        # the most recently checked index was, or if we simply reached
        # the end of the list, set the value at the current index we're
        # comparing against to be the value of the number to be reinserted.
        the_list[current_index_to_compare_against] = number_to_be_reinserted

    return the_list


# Number of times I typed "reinsort" while writing this program: 2


if __name__ == '__main__':

    # "Include an "if __name__ == '__main__':" block at the end of your
    # module that demonstrates the performance characteristics of this
    # sort over a variety of lengths of input in both the best and
    # worst-case scenarios. Executing your module should print informative
    # output about the performance of your sort to the terminal."

    import random

    for each_pass in range(0, 100):
        random_list = []
        for each_number in range(0, random.randint(3, 40)):
            random_number = random.randint(0, random.randint(1, 1000))
            random_list.append(random_number)
        print("\n* * * * *\n\nUnsorted:\n    " + str(random_list))
        sorted_random_list = insertion_sort(random_list)
        print("Sorted:\n    " + str(sorted_random_list))

        assert len(random_list) == len(sorted_random_list)
        for each_number in range(0, (len(sorted_random_list) - 1)):
            assert (sorted_random_list[each_number]
                    <= sorted_random_list[(each_number + 1)])

    print("\n\n===================\nBegin boring tests.\n===================")

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
        sorted_list = insertion_sort(dict_of_lists[each_list])
        print("Sorted:\n    " + str(sorted_list))

    print("\nPerformance is O(n) in the best case O(n^2) in the worst case.")

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
        insertion_sort(sorting_list)
        return_list = []
        for each_number in sorting_list:
            return_list.append(chr(each_number))
        return [''.join(return_list)][0]

    for each_list in strings_dict:
        print("\n* * * * *\n\nUnsorted:\n    " + str(strings_dict[each_list]))
        sorted_list = sort_string(strings_dict[each_list])
        print("Sorted:\n    " + str(sorted_list))

    print
