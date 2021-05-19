import unittest
import random
import os

import main


class TreeOfLifeTest(unittest.TestCase):

    def test_case_regression(self):
        self.assertEqual(main.TreeOfLife(3, 4, 4, [".+..", "..+.", ".+.."]),
                         ['.+..', '..+.', '.+..'])
        self.assertEqual(main.TreeOfLife(1, 1, 5, ["."]),
                         ['+'])
        self.assertEqual(main.TreeOfLife(1, 4, 5, ["..+.."]),
                         ['++++'])
        self.assertEqual(main.TreeOfLife(2, 2, 7, ["++", ".."]),
                         ['++', '++'])


if __name__ == '__main__':
    unittest.main()
