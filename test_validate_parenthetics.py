'''
Test suite for validate_parenthetics.py

Usefully informed about the way unit tests look by:
https://github.com/linsomniac/python-unittest-skeleton/
blob/master/tests/test_skeleton.py

'''

import unittest
import validate_parenthetics as vp


# So the  unit test class is called test_file_name
class test_validate_parenthetics(unittest.TestCase):

    # and the test case method is called test_method_name
    # But what if the method name is the file name? Is this verboten?
    def test_validate_parenthetics_method(self):

        # The program needs several lists to test with, and the unit tests
        # can modify these lists as they go.
        # To be safe, use self.setUp on every new testing call.
        self.assertEquals(1, vp.validate_parenthetics('('))
        self.assertEquals(-1, vp.validate_parenthetics(')'))
        self.assertEquals(0, vp.validate_parenthetics('()'))
        self.assertEquals(0, vp.validate_parenthetics(''))
        self.assertEquals(0, vp.validate_parenthetics('test string'))
        self.assertEquals(0, vp.validate_parenthetics('(test string)'))
        self.assertEquals(1, vp.validate_parenthetics('(test string'))
        self.assertEquals(-1, vp.validate_parenthetics('test string)'))
        self.assertEquals(0, vp.validate_parenthetics('((((()))))'))
        self.assertEquals(0, vp.validate_parenthetics('(()()(()))()'))
        self.assertEquals(1, vp.validate_parenthetics('(())(()()()'))
        self.assertEquals(0, vp.validate_parenthetics('2(1(3)1(5)4), "()"'))

        self.assertRaises(Exception, vp.validate_parenthetics(()))

        with self.assertRaises(TypeError):
            vp.validate_parenthetics(23564)

        with self.assertRaises(TypeError):
            vp.validate_parenthetics(vp.validate_parenthetics(vp.validate_parenthetics('86')))

unittest.main()
