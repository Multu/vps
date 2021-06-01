import unittest
import random
import os

import main


class KeymakerTest(unittest.TestCase):

    def test_case_regression(self):
        self.assertEqual(main.Keymaker(0),  '')
        self.assertEqual(main.Keymaker(1),  '1')
        self.assertEqual(main.Keymaker(2),  '10')
        self.assertEqual(main.Keymaker(3),  '100')
        self.assertEqual(main.Keymaker(4),  '1001')
        self.assertEqual(main.Keymaker(5),  '10010')
        self.assertEqual(main.Keymaker(6),  '100100')
        self.assertEqual(main.Keymaker(7),  '1001000')
        self.assertEqual(main.Keymaker(8),  '10010000')
        self.assertEqual(main.Keymaker(9),  '100100001')
        self.assertEqual(main.Keymaker(10), '1001000010')
        self.assertEqual(main.Keymaker(11), '10010000100')
        self.assertEqual(main.Keymaker(12), '100100001000')
        self.assertEqual(main.Keymaker(13), '1001000010000')
        self.assertEqual(main.Keymaker(14), '10010000100000')
        self.assertEqual(main.Keymaker(15), '100100001000000')


if __name__ == '__main__':
    unittest.main()
