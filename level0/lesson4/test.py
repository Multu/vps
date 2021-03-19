import unittest
import random

import main


class MadMaxTest(unittest.TestCase):

    def test_one(self):
        input = [3]
        output = [3]

        self.assertEqual(main.MadMax(len(input), input), output)

    def test_three(self):
        input = [1, 2, 3]
        output = [1, 3, 2]

        for i in range(100):
            random.shuffle(input)
            self.assertEqual(main.MadMax(len(input), input), output)

    def test_seven(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        output = [1, 2, 3, 7, 6, 5, 4]

        for i in range(100):
            random.shuffle(input)
            self.assertEqual(main.MadMax(len(input), input), output)

    def test_large(self):
        input = list(range(1, 128))
        output = list(range(1, 64)) + list(range(127, 63, -1))

        for i in range(10000):
            random.shuffle(input)
            self.assertEqual(main.MadMax(len(input), input), output)

if __name__ == '__main__':
    unittest.main()
