import unittest
import random

import task1
import task2
import task3
import task4
import task5
import task6
import task7


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

    def test_even_values(self):
        self.assertEqual(task5.even_values([]), [])
        self.assertEqual(task5.even_values([1, 3, 5, 7]), [])
        self.assertEqual(task5.even_values([2, 4, 6, 8, 12]), [2, 4, 6, 8, 12])
        self.assertEqual(task5.even_values([1, 4, 6, 9, 10]), [4, 6, 10])
        self.assertEqual(task5.even_values([0, 4, 4, 4, 7]), [0, 4, 4, 4])

    def test_even_index_values(self):
        self.assertEqual(task6.even_index_values([]), [])
        self.assertEqual(task6.even_index_values([1]), [1])
        self.assertEqual(task6.even_index_values([1, 2]), [1])
        self.assertEqual(task6.even_index_values([1, 2, 3, 4, 5, 6, 7]), [1, 3, 5, 7])
        self.assertEqual(task6.even_index_values([1, 2, 3, 4, 5, 6, 7, 10]), [1, 3, 5, 7])

    def test_second_maximum(self):
        self.assertEqual(task7.second_biggest([]), None)
        self.assertEqual(task7.second_biggest([22]), None)
        self.assertEqual(task7.second_biggest([7, 7]), 7)
        self.assertEqual(task7.second_biggest([5, 5, 5]), 5)
        self.assertEqual(task7.second_biggest([5, 2]), 2)
        self.assertEqual(task7.second_biggest([2, 5]), 2)
        self.assertEqual(task7.second_biggest([4, 6, 8, 14]), 8)
        self.assertEqual(task7.second_biggest([11, 5, 3, 10, 4, 6, 3, 2]), 10)
        self.assertEqual(task7.second_biggest([11, 5, 3, 10, 11, 6, 3, 2]), 11)
        self.assertEqual(task7.second_biggest([11, 11, 3, 10, 4, 11, 6, 3, 2]), 11)



if __name__ == '__main__':
    unittest.main()
