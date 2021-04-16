import unittest
import random

import main


class TankRushTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            [3, 4, '1234 2345 0987', 2, 2, '34 96', False],
            [3, 4, '1234 2345 0987', 2, 2, '34 45', True],
            [3, 4, '1234 2345 0987', 3, 1, '4 5 7', True],
            [3, 4, '1234 2345 0987', 1, 3, '123', True],
            [3, 4, '1234 2345 0987', 1, 2, '24', False],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.TankRush(dataset[0], dataset[1], dataset[2],
                                           dataset[3], dataset[4], dataset[5]),
                             dataset[6])

    def test_empty(self):
        data = [
            [3, 4, '1234 2345 0987', 0, 0, '', True],
            [0, 0, '', 0, 0, '', True],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.TankRush(dataset[0], dataset[1], dataset[2],
                                           dataset[3], dataset[4], dataset[5]),
                             dataset[6])

    def test_equal_size(self):
        data = [
            [3, 4, '1234 2345 0987', 3, 4, '1234 2345 0987', True],
            [3, 4, '1234 2345 0987', 3, 4, '1234 1345 0987', False],
            [3, 4, '1234 2345 0987', 3, 4, '6234 1345 0987', False],
            [2, 2, '12 87', 2, 2, '12 87', True],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.TankRush(dataset[0], dataset[1], dataset[2],
                                           dataset[3], dataset[4], dataset[5]),
                             dataset[6])

    def test_one_char(self):
        data = [
            [3, 4, '1234 2345 0987', 1, 1, '6', False],
            [3, 4, '1234 2345 0987', 1, 1, '1', True],
            [3, 4, '1234 2345 0987', 1, 1, '0', True],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.TankRush(dataset[0], dataset[1], dataset[2],
                                           dataset[3], dataset[4], dataset[5]),
                             dataset[6])

    def test_big_tank_matrix(self):
        data = [
            [2, 2, '12 87', 1, 3, '121', False],
            [2, 2, '12 87', 3, 2, '12 87 11', False],
            [2, 2, '12 87', 3, 3, '122 872 112', False],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.TankRush(dataset[0], dataset[1], dataset[2],
                                           dataset[3], dataset[4], dataset[5]),
                             dataset[6])

if __name__ == '__main__':
    unittest.main()
