import unittest
import random


import main


class DynArray(unittest.TestCase):

    def setUp(self):
        self.dyn_array = main.DynArray()

    def fill_array(self, items):
        for i in range(len(items)):
            self.dyn_array.append(items[i])

    def test_insert_same_capacity_in_head(self):
        init_values = [1, 3, 4, 5]
        self.fill_array(init_values)
        self.dyn_array.insert(0, 8)
        final_values = init_values.copy()
        final_values.insert(0, 8)

        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

    def test_insert_same_capacity_in_tail(self):
        self.fill_array([1, 3, 4, 5])
        self.dyn_array.insert(4, 8)
        correct_result = [1, 3, 4, 5, 8]

        self.assertEqual(self.dyn_array.count, len(correct_result))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(correct_result)):
            self.assertEqual(self.dyn_array[i], correct_result[i])

    def test_insert_same_capacity_in_middle(self):
        self.fill_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.dyn_array.insert(7, 16)
        correct_result = [1, 2, 3, 4, 5, 6, 7, 16, 8, 9, 10, 11, 12, 13, 14, 15]

        self.assertEqual(self.dyn_array.count, len(correct_result))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(correct_result)):
            self.assertEqual(self.dyn_array[i], correct_result[i])

    def test_insert_new_capacity_in_head(self):
        self.fill_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.dyn_array.insert(0, 20)
        correct_result = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        self.assertEqual(self.dyn_array.count, len(correct_result))
        self.assertEqual(self.dyn_array.capacity, 32)
        for i in range(len(correct_result)):
            self.assertEqual(self.dyn_array[i], correct_result[i])

    def test_insert_new_capacity_in_tail(self):
        self.fill_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.dyn_array.insert(16, 20)
        correct_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20]

        self.assertEqual(self.dyn_array.count, len(correct_result))
        self.assertEqual(self.dyn_array.capacity, 32)
        for i in range(len(correct_result)):
            self.assertEqual(self.dyn_array[i], correct_result[i])

    def test_insert_new_capacity_in_middle(self):
        self.fill_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.dyn_array.insert(7, 20)
        correct_result = [1, 2, 3, 4, 5, 6, 7, 20, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        self.assertEqual(self.dyn_array.count, len(correct_result))
        self.assertEqual(self.dyn_array.capacity, 32)
        for i in range(len(correct_result)):
            self.assertEqual(self.dyn_array[i], correct_result[i])

    def test_insert_incorrect_index(self):
        self.fill_array([1, 2, 3, 4, 5])
        with self.assertRaises(IndexError):
            self.dyn_array.insert(7, 20)

    def test_delete_same_capacity_from_head(self):
        init_values = [1, 3, 4, 5]
        self.fill_array(init_values)
        self.dyn_array.delete(0)
        final_values = init_values.copy()
        del final_values[0]

        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

    def test_delete_same_capacity_from_tail(self):
        init_values = [1, 3, 4, 5]
        self.fill_array(init_values)
        self.dyn_array.delete(3)
        final_values = init_values.copy()
        del final_values[3]

        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

    def test_delete_same_capacity_from_middle(self):
        init_values = [1, 3, 4, 5]
        self.fill_array(init_values)
        self.dyn_array.delete(1)
        final_values = init_values.copy()
        del final_values[1]

        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

    def test_delete_new_capacity(self):
        init_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        final_values = init_values.copy()
        self.fill_array(init_values)

        self.dyn_array.delete(5)
        del final_values[5]
        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 32)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

        self.dyn_array.delete(5)
        del final_values[5]
        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 21)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

        for i in range(4):
            self.dyn_array.delete(5)
            del final_values[5]
        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 21)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

        self.dyn_array.delete(5)
        del final_values[5]
        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

        for i in range(4):
            self.dyn_array.delete(5)
            del final_values[5]
        self.assertEqual(self.dyn_array.count, len(final_values))
        self.assertEqual(self.dyn_array.capacity, 16)
        for i in range(len(final_values)):
            self.assertEqual(self.dyn_array[i], final_values[i])

    def test_delete_incorrect_index(self):
        self.fill_array([1, 2, 3, 4, 5])
        with self.assertRaises(IndexError):
            self.dyn_array.delete(5)


if __name__ == '__main__':
    unittest.main()
