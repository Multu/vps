import unittest


import main
import palindrome


class Deque(unittest.TestCase):

    def setUp(self):
        self.deque = main.Deque()

    def test_size(self):
        self.assertEqual(self.deque.size(), 0)

        self.deque.deque = [1, 3, 5, 6, 5]
        self.assertEqual(self.deque.size(), 5)

    def test_add_front(self):
        self.deque.addFront(5)
        self.deque.addFront(6)
        self.deque.addFront(7)
        self.assertEqual(self.deque.size(), 3)
        self.assertEqual(self.deque.peekFront(), 7)
        self.assertEqual(self.deque.peekTail(), 5)

    def test_add_tail(self):
        self.deque.addTail(5)
        self.deque.addTail(6)
        self.deque.addTail(7)
        self.assertEqual(self.deque.size(), 3)
        self.assertEqual(self.deque.peekFront(), 5)
        self.assertEqual(self.deque.peekTail(), 7)

    def test_remove_front(self):
        self.deque.addFront(5)
        self.deque.addFront(6)
        self.deque.addFront(7)

        self.assertEqual(self.deque.removeFront(), 7)
        self.assertEqual(self.deque.removeFront(), 6)
        self.assertEqual(self.deque.removeFront(), 5)
        self.assertEqual(self.deque.removeFront(), None)

    def test_remove_tail(self):
        self.deque.addFront(5)
        self.deque.addFront(6)
        self.deque.addFront(7)

        self.assertEqual(self.deque.removeTail(), 5)
        self.assertEqual(self.deque.removeTail(), 6)
        self.assertEqual(self.deque.removeTail(), 7)
        self.assertEqual(self.deque.removeTail(), None)


class Palindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEqual(palindrome.is_palindrome(''), True)
        self.assertEqual(palindrome.is_palindrome('a'), True)
        self.assertEqual(palindrome.is_palindrome('aa'), True)
        self.assertEqual(palindrome.is_palindrome('aab'), False)
        self.assertEqual(palindrome.is_palindrome('bab'), True)
        self.assertEqual(palindrome.is_palindrome('cbbc'), True)
        self.assertEqual(palindrome.is_palindrome('dddcbacddd'), False)


if __name__ == '__main__':
    unittest.main()
