import unittest
import random

import task1
import task2
import task3
import task4


class RecursionTest(unittest.TestCase):

    def test_exponentiation(self):
        self.assertEqual(task1.exponentiation(0, 0), 1)
        self.assertEqual(task1.exponentiation(2, 5), 32)
        self.assertEqual(task1.exponentiation(8, 2), 64)
        self.assertEqual(task1.exponentiation(4, 1), 4)
        self.assertEqual(task1.exponentiation(18, 0), 1)
        self.assertEqual(task1.exponentiation(3, 4), 81)

    def test_sum_digits(self):
        self.assertEqual(task2.sum_digits(99), 18)
        self.assertEqual(task2.sum_digits(0), 0)
        self.assertEqual(task2.sum_digits(5), 5)
        self.assertEqual(task2.sum_digits(12532), 13)

    def test_list_len(self):
        self.assertEqual(task3.list_len([1, 4, 6, 7, 9]), 5)
        self.assertEqual(task3.list_len([1]), 1)
        self.assertEqual(task3.list_len([]), 0)
        self.assertEqual(task3.list_len(['test', 1, [1, 2]]), 3)

    def test_palindrome(self):
        self.assertEqual(task4.is_palindrome(''), True)
        self.assertEqual(task4.is_palindrome('a'), True)
        self.assertEqual(task4.is_palindrome('12321'), True)
        self.assertEqual(task4.is_palindrome('1234321'), True)
        self.assertEqual(task4.is_palindrome('123421'), False)
        self.assertEqual(task4.is_palindrome('кизик'), True)
        self.assertEqual(task4.is_palindrome('not palindrome'), False)


if __name__ == '__main__':
    unittest.main()
