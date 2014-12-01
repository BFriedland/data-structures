
import random
import unittest
import radix_sort as r_s


class test_RadixSort(unittest.TestCase):

    def test_randomly(self):

        for each_pass in range(0, 1000):

            random_order_of_magnitude = (10 ** random.randint(1, 10))
            random_list = []
            for each_number in range(0, random.randint(3, 40)):
                # E.g., 1000 to 9999 or 10 to 99 or 10000000 to 99999999
                topend = (random_order_of_magnitude * 10) - 1
                random_number = random.randint(random_order_of_magnitude,
                                               topend)
                random_list.append(random_number)
            # Verify the above worked...
            # preferably in the most humorously awkward yet direct way
            for each_number_index in range(1, len(random_list)):
                assert (len(str(random_list[each_number_index]))
                        == (len(str(random_list[(each_number_index - 1)]))))

            sorted_random_list = r_s.radix_sort(random_list)
            assert len(random_list) == len(sorted_random_list)
            for each_number in range(0, (len(sorted_random_list) - 1)):
                assert (sorted_random_list[each_number]
                        <= sorted_random_list[(each_number + 1)])

    def test_predictably(self):

        dict_of_base_two_lists = {
            'list_zero': [0, 0, 0, 0, 0, 0, 0, 0],
            'list_one': [0, 0, 0, 0, 1, 1, 1, 1],
            'list_two': [0, 1, 0, 1, 0, 1, 0, 1],
            'list_three': [0, 1, 1, 0, 1, 1, 0, 0],
            'list_four': [1101, 1110, 1010, 1011, 1100, 1111, 1000, 1001]
        }

        dict_of_base_ten_lists = {
            'list_six': [10, 11, 12, 13, 26, 27, 28, 29],
            'list_four': [56372, 57353, 98124, 12427, 35243, 25352, 53723],
            'list_nine': [26, 27, 28, 29, 10, 11, 12, 13],
            'list_five': [9, 8, 4, 3, 5, 6, 2, 1, 0, 7]
        }

        for each_key in dict_of_base_two_lists:
            each_list = dict_of_base_two_lists[each_key]
            sorted_list = r_s.radix_sort(each_list, base_of_each_digit=2)

            assert len(sorted_list) == len(each_list)

            for each_number in range(0, (len(each_list) - 1)):
                assert (sorted_list[each_number]
                        <= sorted_list[(each_number + 1)])

        for each_key in dict_of_base_ten_lists:
            each_list = dict_of_base_ten_lists[each_key]
            sorted_list = r_s.radix_sort(each_list)

            assert len(sorted_list) == len(each_list)

            for each_number in range(0, (len(each_list) - 1)):
                assert (sorted_list[each_number]
                        <= sorted_list[(each_number + 1)])


unittest.main()
