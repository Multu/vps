import unittest
import random

import main


class UnmannedTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            [10, 2, [[3, 5, 5], [5, 2, 2]], 12],
            [8, 0, [], 8],
            [5, 1, [[2, 0, 0]], 5],
            [0, 0, [], 0],
            [10, 2, [[3, 5, 5], [6, 2, 2]], 14],
            [10, 2, [[3, 5, 5], [4, 2, 2]], 12],
            [10, 4, [[3, 0, 2], [4, 0, 4], [6, 0, 3], [8, 0, 20]], 10],
            [100, 10, [[5, 10, 30], [15, 5, 10], [25, 60, 20], [35, 5, 5], [45, 0, 10], [55, 15, 5], [65, 20, 10], [75, 1, 1], [85, 0, 0], [95, 5, 3]], 146],
            [5, 1, [[17, 9, 1]], 5],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.Unmanned(dataset[0], dataset[1], dataset[2]), dataset[3])

if __name__ == '__main__':
    unittest.main()
