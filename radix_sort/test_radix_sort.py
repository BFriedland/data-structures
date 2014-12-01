
import random
import unittest
import radix_sort as r_s


class test_RadixSort(unittest.TestCase):

    def test_randomly():

        for each_pass in range(0, 1000):

            random_order_of_magnitude = (10 ** random.randint(1, 1))
            random_list = []
            for each_number in range(0, random.randint(3, 40)):
                # E.g., 1000 to 9999 or 10 to 99 or 10000000 to 99999999
                topend = (random_order_of_magnitude * 10) - 1
                random_number = random.randint(random_order_of_magnitude, topend)
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

        dict_of_lists = {
            'list_zero': [0, 0, 0, 0, 0, 0, 0, 0],
            'list_one': [0, 0, 0, 0, 1, 1, 1, 1],
            'list_two': [0, 1, 0, 1, 0, 1, 0, 1],
            'list_three': [0, 1, 1, 0, 1, 1, 0, 0],
            'list_four': [0000010, 0000100, 1000000, 0010000,
                          0000001, 0100000, 0000000, 0001000],
            'list_five': [0001, 0010, 0100, 1000,
                          1100, 0011, 0101, 0110],
        }

        for each_key in dict_of_lists:
            each_list = dict_of_lists[each_key]
            sorted_list = r_s.radix_sort(each_list)

            assert len(sorted_list) == len(each_list)

            for each_number in range(0, (len(each_list) - 1)):
                assert (sorted_list[each_number]
                        <= sorted_list[(each_number + 1)])


unittest.main()
