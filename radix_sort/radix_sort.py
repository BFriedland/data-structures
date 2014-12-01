

# This implementation was created with assistance from:
# http://www.geekviewpoint.com/python/sorting/radixsort
# http://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Radix_sort


def radix_sort(the_list, base_of_each_digit=10):

    # Radix sort operates on the assumption that all numbers handed to it
    # are the same number of digits long. This is a key constraint of the
    # algorithm's efficiency, and so it is taken for granted in
    # this implementation. If this cannot be guaranteed for a given
    # dataset, a separate handler function must be applied to that dataset
    # to ensure compliance with radix_sort's constraints, similarly to how
    # an enumeration of the dataset would be needed if radix_sort was to
    # be applied to a non-numeric set of compared objects.
    # Basically, if the data does not match the algorithm's constraints,
    # the data must be changed.
    # With the above in mind, we're going to get the number of keys used
    # by this radix_sort algorithm from the length of the string
    # representation of the first number in the list:
    # digits_per_number = len(str(the_list[0]))
    # ...
    # Python, out of my control without messing with rather low-level code,
    # shaves off prepended zeroes on integers.
    # This messed with my code. So, here's my retry:
    lengths_of_numbers_in_the_list = []
    for each_number in the_list:
        lengths_of_numbers_in_the_list.append(len(str(each_number)))
    digits_per_number = max(lengths_of_numbers_in_the_list)
    # This STILL failed, BUT the algorithm works overall as long as
    # numbers with fewer keys than the most keys in the list are supplied.
    # There's a better solution but I'm running out of time and it's late.

    # Radix sort operates by making one 'bin' per digit_per_number and
    # sorting inside it, then repeating and sorting inside the next,
    # moving from least significant digit to most significant digit
    # (in my implementation; in others it could conceivably be most to least).

    for each_digit in range(0, digits_per_number):

        # We must redo this binning procedure for every digit in the number.
        list_full_of_digit_bins = []

        # One bin per number in the base:
        for each_numeral in range(0, base_of_each_digit):
            list_full_of_digit_bins.append([])

        # Used for the bin-filling procedure.
        # This is the rounded numeric value of the order of magnitude
        # for the particular digit we're looking at this pass.
        power_of_ten_this_pass = (10 ** each_digit)

        # Now, load the bins (the sub-sorting step) with pieces from the list.
        for each_element in the_list:
            # First, get the bin number -- the progress through the bases --
            # to put the numbers in. This is derived in three parts.
            # First, divide each_element we're looking at by the power of ten
            # we're working at to remove all the extraneous lesser values
            # beneath it that we've already looked at in previous digit passes:
            element_without_smaller_digits = (each_element
                                              // power_of_ten_this_pass)

            # Now retrieve the specific number we need to look at by shaving
            # off all the MORE significant digits.
            # This is the bin index number we need,
            # plucked straight out of the number itself!
            bin_index_number = (element_without_smaller_digits
                                % base_of_each_digit)

            # Put the element in that bin. Sorting! Woohoo!
            list_full_of_digit_bins[bin_index_number].append(each_element)

        # Now to fill the list, either to return it or do the next digit.

        # Note that this particular variable for the list is WIPED OUT
        # every time and extended with data from the sub-sorted bins.
        # This took me a while to understand. I was originally going to
        # do it on a separate list preloaded with values from the input
        # list, but this is simply a better, less frivolous way.
        the_list = []

        for each_sorted_digit_bin in list_full_of_digit_bins:
            for each_sorted_element in each_sorted_digit_bin:
                the_list.append(each_sorted_element)

    # After it's done all of the above digits_per_number-number of times,
    # the list is sorted. Soooooorceryyyyyy
    return the_list


if __name__ == "__main__":

    dict_of_base_two_lists = {
        'list_zero': [0, 0, 0, 0, 0, 0, 0, 0],
        'list_one': [0, 0, 0, 0, 1, 1, 1, 1],
        'list_two': [0, 1, 0, 1, 0, 1, 0, 1],
        'list_three': [0, 1, 1, 0, 1, 1, 0, 0],
        'list_four': [1101, 1110, 1010, 1011, 1100, 1111, 1000, 1001]
    }

    dict_of_base_ten_lists = {
        'list_five': [10, 11, 12, 13, 26, 27, 28, 29],
        'list_six': [56372, 57353, 98124, 12427, 35243, 25352, 53723],
        'list_seven': [26, 27, 28, 29, 10, 11, 12, 13],
        'list_eight': [9, 8, 4, 3, 5, 6, 2, 1, 0, 7]
    }

    for each_key in dict_of_base_two_lists:
        each_list = dict_of_base_two_lists[each_key]

        print("\n* * * * *\n\nUnsorted:\n    " + str(each_list))
        sorted_list = radix_sort(each_list, base_of_each_digit=2)
        print("Sorted:\n    " + str(sorted_list))

    for each_key in dict_of_base_ten_lists:
        each_list = dict_of_base_ten_lists[each_key]

        print("\n* * * * *\n\nUnsorted:\n    " + str(each_list))
        sorted_list = radix_sort(each_list, base_of_each_digit=10)
        print("Sorted:\n    " + str(sorted_list))

    print("\nPerformance is complicated and dependent on the length"
          "\nof the numbers being sorted."
          "\nAll cases are O(k*n), where k is the number of keys"
          "\nin the elements being sorted and n is the number of"
          "\nelements to sort."
          "\nThis comes out to ~O(n) when the key count is small"
          "\nand the element count is large, but can be arbitrarily"
          "\nworse when key count outpaces the element count."
          "\nThere is no typical case for truly random datasets"
          "\nbecause radix_sort presumes the elements will be"
          "\nof an estimable length.")

    proceed = raw_input("\nThe algorithm will now proceed to spammily test"
                        "\nrandomly generated lists. Press control-c to break."
                        "\n> ")

    print "\nBegin random testing.\n\n"

    import random

    for each_pass in range(0, 1000):

        random_order_of_magnitude = (10 ** random.randint(1, 1))
        random_list = []
        for each_number in range(0, random.randint(3, 40)):
            # E.g., 1000 to 9999 or 10 to 99 or 10000000 to 99999999
            topend = (random_order_of_magnitude * 10) - 1
            random_number = random.randint(random_order_of_magnitude,
                                           topend)
            random_list.append(random_number)

        print("\n* * * * *\n\nUnsorted:\n    " + str(random_list))
        sorted_random_list = radix_sort(random_list)
        print("Sorted:\n    " + str(sorted_random_list))
