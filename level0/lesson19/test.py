import unittest
import random

import main


class ShopOLAPTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            [['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4'],
             ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2']],

            [['товар1 5', 'товар12 2', 'товар123 1', 'товар4 3'],
             ['товар1 5', 'товар4 3', 'товар12 2', 'товар123 1']],

            [['товар1 5', 'товар1 2', 'товар1 1', 'товар1 3'],
             ['товар1 11']],

            [['товар1 5'],
             ['товар1 5']],

            [['товар1 5', 'товар1 0', 'товар2 0', 'товар4 1', 'товар3 7'],
             ['товар3 7', 'товар1 5', 'товар4 1', 'товар2 0']],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.ShopOLAP(len(dataset[0]), dataset[0]), dataset[1])

if __name__ == '__main__':
    unittest.main()
