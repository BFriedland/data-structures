# Rotating XOR Hash Table
#
# Author: Ben Friedland << friedland.ben@gmail.com >>
# URL: << http://benfriedland.com/ >>
# GitHub: << github.com/BFriedland >>
# For license information, see LICENSE file.

'''
hash_table.py will allow the construction of HashTable objects
    of user defined sizes that permit only str-type objects for keys.

    The hashing algorithm used combines bit rotation and XOR hashing, and
        was researched from:
        http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_hashing.aspx

    HashTables will accept any positive integer table size; to optimize
        for performance, the user is expected to determine their own ideal
        hash table size, which is likely to be around 1.6 times the size of
        the anticipated inputs, according to people with evaluation criteria
        I have not yet had time to research.

    HashTable objects may be instantiated by calling:
        HashTable(size)

    HashTable methods include:
        get(key)
            Retrieve from the hash table the value associated with
            the given key string.
        set(key, value)
            Set the value for key in the HashTable to refer to value.
        hash(key)
            Return the hash of a given key string.
'''


class HashTable:

    ''' HashTable methods include get(key), set(key, value) and hash(key) '''

    def __init__(self, size):

        self.hash_table = []

        if (not isinstance(size, int)) or (size < 1):
            # HashTables with sizes beneath 1 may cause the god of logic
            # to spontaneously generate black holes in your CPU.
            # Save the Earth by issuing a ValueError:
            raise ValueError("HashTables must have int size >= 1")

        # self.size will be used for the modulus operator's argument:
        self.size = size

        # Initialize the hash_table by filling it with blank lists:
        for each_slot in range(0, self.size):
            self.hash_table.append([])

    def get(self, key):
        ''' Retrieve from the hash table the
        value associated with the given key string. '''

        if not isinstance(key, str):
            raise KeyError("key must be type str")

        index_of_slot_to_retrieve_from = self.hash(key)

        slot_to_retrieve_from = self.hash_table[index_of_slot_to_retrieve_from]

        # Treat every top-level slot as a bucket automatically.
        # Still faster than using an ordinary linked list.
        for each_subslot in slot_to_retrieve_from:
            if each_subslot[0] == key:
                return each_subslot[1]

        raise KeyError("{}".format(key))

    def _return_index_from_inside_bucket(self, key):

        # I decided to make an additonal, internal function so that
        # I wouldn't be putting too much responsibility in the other
        # very similar function get(). Hopefully this is a better practice
        # and not an antipattern.

        if not isinstance(key, str):
            raise KeyError("key must be type str")

        index_of_slot_to_retrieve_from = self.hash(key)

        slot_to_retrieve_from = self.hash_table[index_of_slot_to_retrieve_from]

        # Treat every top-level slot as a bucket automatically.
        # Still faster than using an ordinary linked list.
        for each_subslot_index in range(0, len(slot_to_retrieve_from)):
            if slot_to_retrieve_from[each_subslot_index][0] == key:
                return each_subslot_index

        raise KeyError("{}".format(key))

    def set(self, key, value):
        ''' Set the value for key in the HashTable to refer to value. '''
        if not isinstance(key, str):
            raise KeyError("key must be type str")

        # Cause duplicate keys to overwrite the previous key's value.
        # This is in a try:except block so that we can catch the second
        # kind of KeyError -- where the list is empty -- without raising
        # it to the user, since that information is only used internally.
        try:
            # self._return_index_from_inside_bucket() will raise a KeyError
            # if the key does not yet have any associated values in
            # the hash_table. This error is what the try:except block is
            # here to handle; if it gets no error, the index is used below.
            index_inside_bucket = self._return_index_from_inside_bucket(key)

            # First, hash the key to figure out where to put the value:
            index_of_where_to_put_it = self.hash(key)

            # This slot will always contain a list.
            bucket_to_put_it_in = self.hash_table[index_of_where_to_put_it]

            # Reassign the preexisting value to the new value:
            bucket_to_put_it_in[index_inside_bucket][1] = value

        except KeyError:
            # Then there must be nothing there.
            # Put something there.

            # First, hash the key to figure out where to put the value:
            index_of_where_to_put_it = self.hash(key)

            # This slot will always contain a list.
            bucket_to_put_it_in = self.hash_table[index_of_where_to_put_it]

            # Keys must still be kept track of so we can traverse the
            # subslots ("buckets") as linked lists, comparing keys
            # directly rather than hashes.
            bucket_to_put_it_in.append([key, value])

    def hash(self, key):
        ''' Return the hash of a given key string. '''

        # Informed/partially reinterpreted from:
        # http://www.eternallyconfuzzled.com/
        #    tuts/algorithms/jsw_tut_hashing.aspx
        # Specifically, I'm implementing the byte-rotating XOR algorithm.

        hash_handler = 0

        for each_character in key:
            # First, xor it. (( ref: http://www.eternallyconfuzzled.com ))
            # This is not sufficient on its own, because you'll
            # get some clustering that can be demonstrated by checking
            # the results of simply putting in "a", "b", "c"...
            # and noticing they're all inserted in order.
            # Going some way towards alleviating this problem,
            # we will rotate the hash handler itself, on the bytecode level,
            # so that it has a well-shuffled value.
            # The apparent "randomness" of this comes from the fact that
            # powers of two have a complicated cross-mapping to powers of
            # ten when managed in this way.
            # The arrows are byte rotators:
            # 00000001 << 1 == 00000010
            # 01000100 >> 2 == 00010001
            # etc.
            hash_handler = ((hash_handler << 4)
                            ^ (hash_handler >> 28)
                            ^ ord(each_character))
            # NOTE: This will make some hashes long ints, or type long.
            # It is otherwise just fine and all of that business
            # is handled internally to Python.

        # Probably a good idea to add a big old constant to it.
        # This MIGHT prevent clustering, or it might not, I don't know.
        # Remove if clustering doesn't matter.
        # ...
        # ooooor read about xoring and remember how that works...
        # prehash_character_sum += 10000
        # ...
        # Also, this does not alleviate clustering,
        # it just shifts it some number of places.

        the_hash_value = (hash_handler % self.size)

        return the_hash_value
