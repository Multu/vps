import unittest
import random

import main


class MaximumDiscountTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            [[400, 350, 300, 250, 200, 150, 100], 450],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.MaximumDiscount(len(dataset[0]), dataset[0]), dataset[1])

    def test_without_discount(self):
        data = [
            [[], 0],
            [[300], 0],
            [[100, 200], 0],
            [[100, 200, 0], 0],
            [[100, 200, -200], 0],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.MaximumDiscount(len(dataset[0]), dataset[0]), dataset[1])

    def test_random_price_order(self):
        price = []
        for i in range(100):
            price.append((i + 1) * 10)

        for i in range(1000):
            random.shuffle(price)
            self.assertEqual(main.MaximumDiscount(len(price), price), 16500)


if __name__ == '__main__':
    unittest.main()
