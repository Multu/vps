import unittest
import random
import os

import main


class SherlockValidStringTest(unittest.TestCase):

    def test_case_regression(self):
        self.assertEqual(main.SherlockValidString('xyz'), True)
        self.assertEqual(main.SherlockValidString('xyzaa'), True)
        self.assertEqual(main.SherlockValidString('xxyyz'), True)
        self.assertEqual(main.SherlockValidString('xyzzz'), False)
        self.assertEqual(main.SherlockValidString('xxyyza'), False)
        self.assertEqual(main.SherlockValidString('xxyyzabc'), False)

        self.assertEqual(main.SherlockValidString('abbccc'), False)
        self.assertEqual(main.SherlockValidString('aabbccddabcd'), True)
        self.assertEqual(main.SherlockValidString('aabbbcc'), True)
        self.assertEqual(main.SherlockValidString('aabbbfffcc'), False)
        self.assertEqual(main.SherlockValidString('acccdddfff'), True)

if __name__ == '__main__':
    unittest.main()
