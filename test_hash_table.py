
import unittest
import hash_table

# With some help from:
# https://github.com/jbbrokaw/data-structures/blob/master/test_hashtable.py
import io


class test_HashTable(unittest.TestCase):

    def setUp(self):
        ''' Test the HashTable constructor and
        prepare several tables for other tests. '''

        # If the algorithm works, tables could be any
        # positive integer length.

        self.size_one_hashtable = hash_table.HashTable(1)
        self.size_three_hashtable = hash_table.HashTable(3)
        self.size_ten_thousand_hashtable = hash_table.HashTable(10000)

    def test_hash(self):

        self.setUp()

        assert (self.size_one_hashtable.hash("Size one tables' hashes")
                == self.size_one_hashtable.hash("are always identical."))

        assert (self.size_ten_thousand_hashtable.hash("Larger hashtables")
                != self.size_ten_thousand_hashtable.hash("have many misses."))

        assert isinstance(
            self.size_one_hashtable.hash("All hashes on all tables"),
            (long, int))

        assert isinstance(
            self.size_three_hashtable.hash("should always return"),
            (long, int))

        assert isinstance(
            self.size_ten_thousand_hashtable.hash("an int or long result."),
            (long, int))

    def test_set_and_get_together(self):

        # get() and set() can be co-verified by checking if they have
        # a functionality space equal to that of the expected hash table
        # when they are tested for compliance and failure modes
        # that, together, exclude anything that is not functionally
        # an instance of a hash table with the expected properties.

        self.setUp()

        # Trivial input failures.
        # get() from empty table:
        with self.assertRaises(KeyError):
            self.size_one_hashtable.get("No keys yet added.")
        with self.assertRaises(KeyError):
            self.size_three_hashtable.get("No keys yet added.")
        with self.assertRaises(KeyError):
            self.size_ten_thousand_hashtable.get("No keys yet added.")

        # set() with no value:
        with self.assertRaises(TypeError):
            self.size_one_hashtable.set("Set must take a value.")
        with self.assertRaises(TypeError):
            self.size_three_hashtable.set("Set must take a value.")
        with self.assertRaises(TypeError):
            self.size_ten_thousand_hashtable.set("Set must take a value.")

        # set() with non-string key:
        with self.assertRaises(KeyError):
            self.size_one_hashtable.set(42, "Keys must be strings.")
        with self.assertRaises(KeyError):
            self.size_three_hashtable.set(42, "Keys must be strings.")
        with self.assertRaises(KeyError):
            self.size_ten_thousand_hashtable.set(42, "Keys must be strings.")

        # set()ing and get()ing:
        self.size_one_hashtable.set("One", 146346)
        self.size_one_hashtable.set("Two", "2")
        self.size_one_hashtable.set("T h r e e", 6)

        assert (self.size_one_hashtable.get("One") == 146346)
        assert (self.size_one_hashtable.get("Two") == "2")
        assert (self.size_one_hashtable.get("T h r e e") == 6)

        assert (self.size_one_hashtable.get("One") != 2222222)
        assert (self.size_one_hashtable.get("Two") != "146346")
        assert (self.size_one_hashtable.get("T h r e e") != "six")

        # Re-set()ing:
        self.size_one_hashtable.set("One", 146346)
        self.size_one_hashtable.set("Two", "no.")
        self.size_one_hashtable.set("T h r e e", 555555)

        assert (self.size_one_hashtable.get("One") == 146346)
        assert (self.size_one_hashtable.get("Two") == "no.")
        assert (self.size_one_hashtable.get("T h r e e") == 555555)

        assert (self.size_one_hashtable.get("One") != 2222222)
        assert (self.size_one_hashtable.get("Two") != "146346")
        assert (self.size_one_hashtable.get("T h r e e") != 6)

        # set()ing and get()ing:
        self.size_three_hashtable.set("One", 146346)
        self.size_three_hashtable.set("Two", "2")
        self.size_three_hashtable.set("T h r e e", 6)

        assert (self.size_three_hashtable.get("One") == 146346)
        assert (self.size_three_hashtable.get("Two") == "2")
        assert (self.size_three_hashtable.get("T h r e e") == 6)

        assert (self.size_three_hashtable.get("One") != 2222222)
        assert (self.size_three_hashtable.get("Two") != "146346")
        assert (self.size_three_hashtable.get("T h r e e") != "six")

        # Re-set()ing:
        self.size_three_hashtable.set("One", 146346)
        self.size_three_hashtable.set("Two", "no.")
        self.size_three_hashtable.set("T h r e e", 555555)

        assert (self.size_three_hashtable.get("One") == 146346)
        assert (self.size_three_hashtable.get("Two") == "no.")
        assert (self.size_three_hashtable.get("T h r e e") == 555555)

        assert (self.size_three_hashtable.get("One") != 2222222)
        assert (self.size_three_hashtable.get("Two") != "146346")
        assert (self.size_three_hashtable.get("T h r e e") != 6)

        # set()ing and get()ing:
        self.size_ten_thousand_hashtable.set("One", 146346)
        self.size_ten_thousand_hashtable.set("Two", "2")
        self.size_ten_thousand_hashtable.set("T h r e e", 6)

        assert (self.size_ten_thousand_hashtable.get("One") == 146346)
        assert (self.size_ten_thousand_hashtable.get("Two") == "2")
        assert (self.size_ten_thousand_hashtable.get("T h r e e") == 6)

        assert (self.size_ten_thousand_hashtable.get("One") != 2222222)
        assert (self.size_ten_thousand_hashtable.get("Two") != "146346")
        assert (self.size_ten_thousand_hashtable.get("T h r e e") != "six")

        # Re-set()ing:
        self.size_ten_thousand_hashtable.set("One", 146346)
        self.size_ten_thousand_hashtable.set("Two", "no.")
        self.size_ten_thousand_hashtable.set("T h r e e", 555555)

        assert (self.size_ten_thousand_hashtable.get("One") == 146346)
        assert (self.size_ten_thousand_hashtable.get("Two") == "no.")
        assert (self.size_ten_thousand_hashtable.get("T h r e e") == 555555)

        assert (self.size_ten_thousand_hashtable.get("One") != 2222222)
        assert (self.size_ten_thousand_hashtable.get("Two") != "146346")
        assert (self.size_three_hashtable.get("T h r e e") != 6)

    def test_on_a_long_list_of_words(self):

        # This section heavily styled after:
        # https://github.com/jbbrokaw/
        #   data-structures/blob/master/test_hashtable.py

        word_list_location = '/usr/share/dict/words'

        # Before beginning to iterate through a file using a while loop,
        # initialize each_word so that it won't fail immediately:
        each_word = "Non-null value."

        # First, figure out the ideal size for maximizing the performance
        # of the resulting hash table.

        # Figure out how many words are there:
        word_count = 0
        with io.open(word_list_location) as file_full_of_words:
            # Terminate at end of file:
            while each_word != "":
                each_word = file_full_of_words.readline().strip()
                word_count += 1

        # According to The Powers That Be, we must now multiply the expected
        # size of the hash table by one point six to divine the value of
        # the ideal size of the hash table for performance purposes.
        # Note that HashTable size must be integerized BEFORE construction.
        calculated_hashtable_size = int(word_count * 1.6)

        big_huge_hashtable = hash_table.HashTable(calculated_hashtable_size)

        with io.open(word_list_location) as file_full_of_words:
            while each_word != "":
                each_word = file_full_of_words.readline().strip()
                # Make keys and values identical to ease testing this monster:
                big_huge_hashtable.set(each_word, each_word)

        # Now that the table is compiled, ensure the hasher
        # relates words to the file as expected.
        with io.open(word_list_location) as file_full_of_words:
            while each_word != "":
                each_word = file_full_of_words.readline().strip()
                assert big_huge_hashtable.get(each_word) == each_word


unittest.main()
