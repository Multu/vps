import unittest
import random

import main


class Heap(unittest.TestCase):

    def setUp(self):
        self.heap = main.Heap()

    def test_make_heap(self):
        self.heap.MakeHeap([4, 3, 8, 9, 5], 1)
        self.assertEqual(self.heap.HeapArray, [8, 3, 4])

        self.heap.MakeHeap([4, 3, 8, 9, 5], 2)
        self.assertEqual(self.heap.HeapArray, [9, 8, 4, 3, 5, None, None])

    def test_get_max(self):
        self.heap.HeapArray = [9, 8, 4, 3, 5, None, None]

        self.assertEqual(self.heap.GetMax(), 9)
        self.assertEqual(self.heap.HeapArray, [8, 5, 4, 3, None, None, None])

        self.assertEqual(self.heap.GetMax(), 8)
        self.assertEqual(self.heap.HeapArray, [5, 3, 4, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 5)
        self.assertEqual(self.heap.HeapArray, [4, 3, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 4)
        self.assertEqual(self.heap.HeapArray, [3, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 3)
        self.assertEqual(self.heap.HeapArray, [None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), -1)
        self.assertEqual(self.heap.HeapArray, [None, None, None, None, None, None, None])

    def test_add(self):
        self.heap.HeapArray = [9, 8, 4, 3, 5, None, None]

        self.assertEqual(self.heap.Add(7), True)
        self.assertEqual(self.heap.HeapArray, [9, 8, 7, 3, 5, 4, None])

        self.assertEqual(self.heap.Add(6), True)
        self.assertEqual(self.heap.HeapArray, [9, 8, 7, 3, 5, 4, 6])

        self.assertEqual(self.heap.Add(11), False)
        self.assertEqual(self.heap.HeapArray, [9, 8, 7, 3, 5, 4, 6])

if __name__ == '__main__':
    unittest.main()
