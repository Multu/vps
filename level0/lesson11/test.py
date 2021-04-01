import unittest
import random

import main


class BigMinusTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            ['0', '0', '0'],
            ['10', '0', '10'],
            ['3', '7', '4'],
            ['10000000000000000', '9999999999999999', '1'],
            ['10000000000000000', '10000000000000000', '0'],
            ['1234567891', '1', '1234567890'],
            ['1', '321', '320'],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.BigMinus(dataset[0], dataset[1]), dataset[2])

    def test_random(self):
        for i in range(100000):
            n1 = random.randint(0, 10 ** 16)
            n2 = random.randint(0, 10 ** 16)
            sub_str = str(abs(n2 - n1))

            self.assertEqual(main.BigMinus(str(n1), str(n2)), sub_str)


if __name__ == '__main__':
    unittest.main()
