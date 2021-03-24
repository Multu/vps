import unittest
import random

import main


class PatternUnlockTest(unittest.TestCase):

    def test_example(self):
        hits = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]
        output = '982843'
        self.assertEqual(main.PatternUnlock(len(hits), hits), output)
        self.assertIsInstance(main.PatternUnlock(len(hits), hits), str)

    def test_one_digit(self):
        hits = [2]
        output = ''
        self.assertEqual(main.PatternUnlock(len(hits), hits), output)

    def test_empty(self):
        hits = []
        output = ''
        self.assertEqual(main.PatternUnlock(len(hits), hits), output)

    def test_large_code(self):
        hits = [6, 1, 9, 2, 1, 6, 5, 3, 8, 7, 2 ,6, 1, 9]
        output = '15717'
        self.assertEqual(main.PatternUnlock(len(hits), hits), output)

if __name__ == '__main__':
    unittest.main()
