import unittest


import main
import rotate_queue
import stacked_queue


class Queue(unittest.TestCase):

    def setUp(self):
        self.queue = main.Queue()

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)

        self.queue.queue = [1, 3, 5, 6, 5]
        self.assertEqual(self.queue.size(), 5)

    def test_enqueue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        self.assertEqual(self.queue.queue, [7, 6, 5])

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), None)

        self.queue.queue = [1, 2, 3]
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), None)
        self.assertEqual(self.queue.dequeue(), None)


class RotateQueue(unittest.TestCase):

    def setUp(self):
        self.queue = main.Queue()

    def test_rotate_queue(self):
        self.queue.queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        rotate_queue.rotate_queue(self.queue, 0)
        self.assertEqual(self.queue.queue, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        rotate_queue.rotate_queue(self.queue, 1)
        self.assertEqual(self.queue.queue, [9, 1, 2, 3, 4, 5, 6, 7, 8])

        rotate_queue.rotate_queue(self.queue, 3)
        self.assertEqual(self.queue.queue, [6, 7, 8, 9, 1, 2, 3, 4, 5])


class StackedQueue(unittest.TestCase):

    def setUp(self):
        self.stacked_queue = stacked_queue.StackedQueue()

    def test_size(self):
        self.assertEqual(self.stacked_queue.size(), 0)

        self.stacked_queue.push_stack.stack = [1, 3, 5, 6, 5]
        self.assertEqual(self.stacked_queue.size(), 5)

    def test_enqueue(self):
        self.stacked_queue.enqueue(5)
        self.stacked_queue.enqueue(6)
        self.stacked_queue.enqueue(7)
        self.assertEqual(self.stacked_queue.push_stack.stack, [5, 6, 7])

    def test_dequeue(self):
        self.assertEqual(self.stacked_queue.dequeue(), None)

        self.stacked_queue.push_stack.stack = [1, 2, 3]
        self.assertEqual(self.stacked_queue.dequeue(), 1)
        self.assertEqual(self.stacked_queue.push_stack.stack, [])
        self.assertEqual(self.stacked_queue.pop_stack.stack, [3, 2])

        self.assertEqual(self.stacked_queue.dequeue(), 2)
        self.assertEqual(self.stacked_queue.dequeue(), 3)
        self.assertEqual(self.stacked_queue.dequeue(), None)
        self.assertEqual(self.stacked_queue.dequeue(), None)


if __name__ == '__main__':
    unittest.main()
