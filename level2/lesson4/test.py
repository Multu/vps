import unittest


import main
import reverse_stack
import brackets
import expression


class Stack(unittest.TestCase):

    def setUp(self):
        self.stack = main.Stack()

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)

        self.stack.stack = [1, 3, 5, 6, 5]
        self.assertEqual(self.stack.size(), 5)


    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)

        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.pop(), None)

    def test_push(self):
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(7)
        self.assertEqual(self.stack.stack, [5, 6, 7])

    def test_peek(self):
        self.assertEqual(self.stack.peek(), None)

        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.peek(), 3)


class ReverseStack(unittest.TestCase):

    def setUp(self):
        self.stack = reverse_stack.ReverseStack()

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)

        self.stack.stack = [1, 3, 5, 6, 5]
        self.assertEqual(self.stack.size(), 5)


    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)

        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.pop(), None)

    def test_push(self):
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(7)
        self.assertEqual(self.stack.stack, [7, 6, 5])

    def test_peek(self):
        self.assertEqual(self.stack.peek(), None)

        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.peek(), 1)


class BracketsBalance(unittest.TestCase):

    def test_is_brackets_in_balance(self):
        self.assertEqual(brackets.is_brackets_in_balance('(()((())()))'), True)
        self.assertEqual(brackets.is_brackets_in_balance('(()()(()))'), True)
        self.assertEqual(brackets.is_brackets_in_balance('())('), False)
        self.assertEqual(brackets.is_brackets_in_balance('))(('), False)
        self.assertEqual(brackets.is_brackets_in_balance('((())'), False)


class Expression(unittest.TestCase):

    def test_is_brackets_in_balance(self):
        self.assertEqual(expression.evaluate_expression('8 2 + 5 * 9 + ='), 59)
        self.assertEqual(expression.evaluate_expression('1 2 + 3 * ='), 9)

        with self.assertRaises(RuntimeError):
            expression.evaluate_expression('8 2 10 + 5 * 9 + =')

        with self.assertRaises(RuntimeError):
            expression.evaluate_expression('9 = 2')

        with self.assertRaises(RuntimeError):
            expression.evaluate_expression('10 3')

        with self.assertRaises(ValueError):
            expression.evaluate_expression('2 10 - 5 * 9 + =')

        with self.assertRaises(ValueError):
            expression.evaluate_expression('')


if __name__ == '__main__':
    unittest.main()
