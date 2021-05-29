import unittest
import random
import os

import main


class FootballTest(unittest.TestCase):

    def test_case_regression(self):
        self.assertEqual(main.Football([1, 3, 2], 3), True)
        self.assertEqual(main.Football([1, 2, 3], 3), False)
        self.assertEqual(main.Football([3, 2, 1], 3), True)
        self.assertEqual(main.Football([1, 7, 5, 3, 9], 5), True)
        self.assertEqual(main.Football([9, 5, 3, 7, 1], 5), False)
        self.assertEqual(main.Football([1, 4, 3, 2, 5], 5), True)
        self.assertEqual(main.Football([4], 1), False)
        self.assertEqual(main.Football([2, 5], 2), False)
        self.assertEqual(main.Football([6, 1], 2), True)
        self.assertEqual(main.Football([1, 5, 2, 4, 3, 6, 7], 7), False)


if __name__ == '__main__':
    unittest.main()
