

def quicksort(the_list):

    # References used:
    #   http://en.wikipedia.org/wiki/Quicksort
    # In particular, the "qsort1" example at:
    #   http://en.literateprograms.org/Quicksort_%28Python%29
    # was about one thousand times easier to understand than all the rest;
    # so much so that I don't understand why it's presented any other way.
    # It's possibly the cleanest sorting algorithm implementation I've
    # ever seen and I recommend it fully.

    # This doesn't work -- it fails on empty lists.
    # if len(the_list) < 2:
    #     return the_list
    # It turns out you need to check for empty listness.
    if the_list == []:
        return the_list

    # Grab the zeroeth element in the list and make it the pivot point:
    pivot_value = the_list[0]

    values_lesser_than_the_pivot = []
    values_greater_than_the_pivot = []

    # The zeroeth element is the pivot, so skip it with list slicing:
    for each_element in the_list[1:]:

        if each_element < pivot_value:
            values_lesser_than_the_pivot.append(each_element)
        else:
            values_greater_than_the_pivot.append(each_element)

    sorted_values_lesser_than_the_pivot \
        = quicksort(values_lesser_than_the_pivot)

    sorted_values_greater_than_the_pivot \
        = quicksort(values_greater_than_the_pivot)

    sorted_list = []

    # Joining the sub-lists together:
    if sorted_values_lesser_than_the_pivot is not None:
        sorted_list += sorted_values_lesser_than_the_pivot

    # The pivot value isn't in a list before this point.
    # In order to use the concatenation operator, all values below
    # must be inside a list, so we must spot-listify it.
    sorted_list += [pivot_value]

    if sorted_values_greater_than_the_pivot is not None:
        sorted_list += sorted_values_greater_than_the_pivot

    # Note to self: Don't forget about commented return statements
    # in recursive functions when trying to debug them.
    return sorted_list


if __name__ == '__main__':

    # "Include an "if __name__ == '__main__':" block at the end of your
    # module that demonstrates the performance characteristics of this
    # sort over a variety of lengths of input in both the best and
    # worst-case scenarios. Executing your module should print informative
    # output about the performance of your sort to the terminal."

    # Sorted is sorted, so I'm going to copy my insertion_sort tests and
    # use the quicksort algorithm on them.

    import random

    for each_pass in range(0, 100):
        random_list = []
        for each_number in range(0, random.randint(3, 40)):
            random_number = random.randint(0, random.randint(1, 1000))
            random_list.append(random_number)
        print("\n* * * * *\n\nUnsorted:\n    " + str(random_list))
        sorted_random_list = quicksort(random_list)
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
        sorted_list = quicksort(dict_of_lists[each_list])
        print("Sorted:\n    " + str(sorted_list))

    print("\nPerformance is O(nlogn) in the best and average cases,\n"
          "and O(n^2) in the worst case.")

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
        sorting_list = quicksort(sorting_list)
        return_list = []
        for each_number in sorting_list:
            return_list.append(chr(each_number))
        return [''.join(return_list)][0]

    for each_list in strings_dict:
        print("\n* * * * *\n\nUnsorted:\n    " + str(strings_dict[each_list]))
        sorted_list = sort_string(strings_dict[each_list])
        print("Sorted:\n    " + str(sorted_list))

    print
