import unittest
import random
import os

import main


class BastShoeTest(unittest.TestCase):

    def tearDown(self):
        main.history = ['']
        main.pointer = 0
        main.undo_state = False


    def test_case1(self):
        self.assertEqual(main.BastShoe('1 Привет'), 'Привет')
        self.assertEqual(main.BastShoe('1 , Мир!'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('1 ++'), 'Привет, Мир!++')
        self.assertEqual(main.BastShoe('2 2'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('4'), 'Привет, Мир!++')
        self.assertEqual(main.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('1 *'), 'Привет, Мир!*')
        self.assertEqual(main.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('3 6'), ',')
        self.assertEqual(main.BastShoe('2 100'), '')
        self.assertEqual(main.BastShoe('1 Привет'), 'Привет')
        self.assertEqual(main.BastShoe('1 , Мир!'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('1 ++'), 'Привет, Мир!++')
        self.assertEqual(main.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('4'), 'Привет')
        self.assertEqual(main.BastShoe('5'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('4'), 'Привет')
        self.assertEqual(main.BastShoe('5'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('5'), 'Привет, Мир!++')
        self.assertEqual(main.BastShoe('5'), 'Привет, Мир!++')
        self.assertEqual(main.BastShoe('5'), 'Привет, Мир!++')
        self.assertEqual(main.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(main.BastShoe('4'), 'Привет')
        self.assertEqual(main.BastShoe('2 2'), 'Прив')
        self.assertEqual(main.BastShoe('4'), 'Привет')
        self.assertEqual(main.BastShoe('5'), 'Прив')
        self.assertEqual(main.BastShoe('5'), 'Прив')
        self.assertEqual(main.BastShoe('5'), 'Прив')

    def test_case2(self):
        self.assertEqual(main.BastShoe('1 Зарядка'), 'Зарядка')
        self.assertEqual(main.BastShoe('1  для ума'), 'Зарядка для ума')
        self.assertEqual(main.BastShoe('2 4'), 'Зарядка для')
        self.assertEqual(main.BastShoe('1  меня'), 'Зарядка для меня')
        self.assertEqual(main.BastShoe('4'), 'Зарядка для')
        self.assertEqual(main.BastShoe('4'), 'Зарядка для ума')
        self.assertEqual(main.BastShoe('3 3'), 'я')
        self.assertEqual(main.BastShoe('1  молодец'), 'Зарядка для ума молодец')
        self.assertEqual(main.BastShoe('2 8'), 'Зарядка для ума')
        self.assertEqual(main.BastShoe('5'), 'Зарядка для ума')
        self.assertEqual(main.BastShoe('4'), 'Зарядка для ума молодец')

    def test_case3(self):
        self.assertEqual(main.BastShoe('1 Мастер'), 'Мастер')
        self.assertEqual(main.BastShoe('1  И Маргарита'), 'Мастер И Маргарита')
        self.assertEqual(main.BastShoe('1 ?!'), 'Мастер И Маргарита?!')
        self.assertEqual(main.BastShoe('2 5'), 'Мастер И Маргар')
        self.assertEqual(main.BastShoe('4'), 'Мастер И Маргарита?!')
        self.assertEqual(main.BastShoe('4'), 'Мастер И Маргарита')
        self.assertEqual(main.BastShoe('5'), 'Мастер И Маргарита?!')
        self.assertEqual(main.BastShoe('5'), 'Мастер И Маргар')
        self.assertEqual(main.BastShoe('5'), 'Мастер И Маргар')
        self.assertEqual(main.BastShoe('2 2'), 'Мастер И Марг')
        self.assertEqual(main.BastShoe('3 11'), 'р')
        self.assertEqual(main.BastShoe('1 оман.'), 'Мастер И Маргоман.')
        self.assertEqual(main.BastShoe('2 30'), '')
        self.assertEqual(main.BastShoe('1 классика'), 'классика')
        self.assertEqual(main.BastShoe('3 15'), '')

    def test_case4(self):
        self.assertEqual(main.BastShoe('1 Зарядка'), 'Зарядка')
        self.assertEqual(main.BastShoe('1  для ума'), 'Зарядка для ума')
        self.assertEqual(main.BastShoe('2 4'), 'Зарядка для')
        self.assertEqual(main.BastShoe('1  меня'), 'Зарядка для меня')
        self.assertEqual(main.BastShoe('4'), 'Зарядка для')
        self.assertEqual(main.BastShoe('4'), 'Зарядка для ума')
        self.assertEqual(main.BastShoe('3 3'), 'я')
        self.assertEqual(main.BastShoe('4'), 'Зарядка')
        self.assertEqual(main.BastShoe('7 (некорректная команда)'), 'Зарядка')
        self.assertEqual(main.BastShoe('1 !'), 'Зарядка!')

    def test_case5(self):
        self.assertEqual(main.BastShoe('1 a'), 'a')
        self.assertEqual(main.BastShoe('1 b'), 'ab')
        self.assertEqual(main.BastShoe('1 c'), 'abc')
        self.assertEqual(main.BastShoe('2 5'), '')
        self.assertEqual(main.BastShoe('4'), 'abc')
        self.assertEqual(main.BastShoe('3 0'), 'a')
        self.assertEqual(main.BastShoe('4'), 'ab')
        self.assertEqual(main.BastShoe('3 -1'), '')
        self.assertEqual(main.BastShoe('3 (некорректный параметр)'), '')
        self.assertEqual(main.BastShoe('1 один'), 'abодин')
        self.assertEqual(main.BastShoe('3 0'), 'a')
        self.assertEqual(main.BastShoe('3 20'), '')

    def test_case6(self):
        self.assertEqual(main.BastShoe('3 10'), '')
        self.assertEqual(main.BastShoe('1 привет'), 'привет')
        self.assertEqual(main.BastShoe('3 5'), 'т')
        self.assertEqual(main.BastShoe('3 1'), 'р')
        self.assertEqual(main.BastShoe('1 два'), 'приветдва')
        self.assertEqual(main.BastShoe('3 ааа'), '')
        self.assertEqual(main.BastShoe('1 ааа'), 'приветдваааа')
        self.assertEqual(main.BastShoe('10 ааа'), 'приветдваааа')
        self.assertEqual(main.BastShoe('3 '), '')

    def test_case7(self):
        self.assertEqual(main.BastShoe('1 a'), 'a')
        self.assertEqual(main.BastShoe('1 b'), 'ab')
        self.assertEqual(main.BastShoe('1 c'), 'abc')
        self.assertEqual(main.BastShoe('1 d'), 'abcd')
        self.assertEqual(main.BastShoe('1 e'), 'abcde')
        self.assertEqual(main.BastShoe('3 0'), 'a')
        self.assertEqual(main.BastShoe('3 4'), 'e')


if __name__ == '__main__':
    unittest.main()
