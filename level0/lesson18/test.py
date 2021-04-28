import unittest
import random

import main


class MisterRobotTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            [[1, 3, 4, 5, 6, 2, 7], True],
            [[1, 2, 3, 5, 4], False],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9], True],
            [[9, 8, 7, 6, 5, 4, 3, 2, 1], True],
            [[6, 5, 4, 3, 2, 1], False],
            [[2, 5, 7, 9, 1, 6, 4, 3, 8], True],
            [[9, 2, 1, 3, 5, 8, 4, 6, 7], False],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.MisterRobot(len(dataset[0]), dataset[0]), dataset[1])

if __name__ == '__main__':
    unittest.main()
