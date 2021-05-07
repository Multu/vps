import unittest
import random
import os

import main


class BastShoeTest(unittest.TestCase):

    def tearDown(self):
        os.remove(main.history_filename)
        os.remove(main.pointer_filename)

    def test_case1(self):
        data = [
            ['1 Привет', 'Привет'],
            ['1 , Мир!', 'Привет, Мир!'],
            ['1 ++', 'Привет, Мир!++'],
            ['2 2', 'Привет, Мир!'],
            ['4', 'Привет, Мир!++'],
            ['4', 'Привет, Мир!'],
            ['1 *', 'Привет, Мир!*'],
            ['4', 'Привет, Мир!'],
            ['4', 'Привет, Мир!'],
            ['4', 'Привет, Мир!'],
            ['3 6', ','],
            ['2 100', ''],
            ['1 Привет', 'Привет'],
            ['1 , Мир!', 'Привет, Мир!'],
            ['1 ++', 'Привет, Мир!++'],
            ['4', 'Привет, Мир!'],
            ['4', 'Привет'],
            ['5', 'Привет, Мир!'],
            ['4', 'Привет'],
            ['5', 'Привет, Мир!'],
            ['5', 'Привет, Мир!++'],
            ['5', 'Привет, Мир!++'],
            ['5', 'Привет, Мир!++'],
            ['4', 'Привет, Мир!'],
            ['4', 'Привет'],
            ['2 2', 'Прив'],
            ['4', 'Привет'],
            ['5', 'Прив'],
            ['5', 'Прив'],
            ['5', 'Прив'],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.BastShoe(dataset[0]), dataset[1], msg=f'{i+1} line')

    def test_case2(self):
        data = [
            ['1 Зарядка', 'Зарядка'],
            ['1  для ума', 'Зарядка для ума'],
            ['2 4', 'Зарядка для'],
            ['1  меня', 'Зарядка для меня'],
            ['4', 'Зарядка для'],
            ['4', 'Зарядка для ума'],
            ['3 3', 'я'],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.BastShoe(dataset[0]), dataset[1], msg=f'{i+1} line')

    def test_case3(self):
        data = [
            ['5', ''],
            ['5', ''],
            ['4', ''],
            ['1 тест', 'тест'],
            ['4', ''],
            ['2', ''],
            ['3 3', ''],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.BastShoe(dataset[0]), dataset[1], msg=f'{i+1} line')

    def test_case4(self):
        data = [
            ['4', ''],
            ['5', ''],
            ['4', ''],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.BastShoe(dataset[0]), dataset[1], msg=f'{i+1} line')

    def test_case5(self):
        data = [
            ['2 3', ''],
            ['1 тест', 'тест'],
            ['4', ''],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.BastShoe(dataset[0]), dataset[1], msg=f'{i+1} line')

    def test_case6(self):
        data = [
            ['3 4', ''],
            ['1 тест', 'тест'],
            ['5', 'тест'],
            ['4', ''],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.BastShoe(dataset[0]), dataset[1], msg=f'{i+1} line')

if __name__ == '__main__':
    unittest.main()
