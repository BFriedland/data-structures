
import random
import unittest
import quicksort as qs


class test_Quicksort(unittest.TestCase):

    def test_randomly(self):

        for each_pass in range(0, 1000):
            random_list = []
            for each_number in range(0, random.randint(3, 40)):
                random_number = random.randint(0, random.randint(1, 1000))
                random_list.append(random_number)
            sorted_random_list = qs.quicksort(random_list)
            assert len(random_list) == len(sorted_random_list)
            for each_number in range(0, (len(sorted_random_list) - 1)):
                assert (sorted_random_list[each_number]
                        <= sorted_random_list[(each_number + 1)])

    def test_predictably(self):

        dict_of_lists = {
            'list_zero': [0, 0, 0, 0, 0, 0, 0, 0],
            'list_one': [0, 0, 0, 0, 1, 1, 1, 1],
            'list_two': [0, 1, 0, 1, 0, 1, 0, 1],
            'list_three': [0, 1, 1, 0, 1, 1, 0, 0],
            'list_four': [10, 100, 1000000, 10000, 1, 100000, 0, 1000],
            'list_five': [0001, 0010, 0100, 1000, 1100, 0011, 0101, 0110],
        }

        for each_key in dict_of_lists:
            each_list = dict_of_lists[each_key]
            sorted_list = qs.quicksort(each_list)

            assert len(sorted_list) == len(each_list)

            for each_number in range(0, (len(each_list) - 1)):
                assert (sorted_list[each_number]
                        <= sorted_list[(each_number + 1)])


unittest.main()
