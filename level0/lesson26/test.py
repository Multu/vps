import unittest
import random
import os

import main


class BalancedParenthesesTest(unittest.TestCase):

    def test_case_regression(self):
        output = main.BalancedParentheses(1).split(' ')
        self.assertEqual(output.sort(), '()'.split(' ').sort())

        output = main.BalancedParentheses(2).split(' ')
        self.assertEqual(output.sort(), '()() (())'.split(' ').sort())

        output = main.BalancedParentheses(3).split(' ')
        self.assertEqual(output.sort(), '((())) ()(()) (())() ()()() (()())'.split(' ').sort())

        output = main.BalancedParentheses(4).split(' ')
        self.assertEqual(output.sort(), '(((()))) ((()())) ((())()) (()(())) (()()()) ((()))() (()())() (())(()) (())()() ()((())) ()(()()) ()(())() ()()(()) ()()()()'.split(' ').sort())


if __name__ == '__main__':
    unittest.main()
