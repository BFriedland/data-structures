

# This implementation was created with assistance from:
# http://www.geekviewpoint.com/python/sorting/radixsort


def radix_sort(the_list):

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
    digits_per_number = len(str(the_list[0]))

    # Radix sort operates by making one 'bucket' per digit_per_number.
    #
    for each_digit in range(0, digits_per_number):

        pass



    # Development on hold because I need to sleep for class tomorrow.




