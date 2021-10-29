import random
import unittest


import main


class OrderedList(unittest.TestCase):

    def setUp(self):
        self.asc_list = main.OrderedList(True)
        self.desc_list = main.OrderedList(False)

    def test_add_asc_to_empty(self):
        self.asc_list.add(5)

        self.assertEqual(self.asc_list.head.value, 5)
        self.assertEqual(self.asc_list.tail.value, 5)
        self.assertEqual(self.asc_list.len(), 1)

    def test_add_asc_in_head(self):
        self.asc_list.add(5)
        self.asc_list.add(2)

        self.assertEqual(self.asc_list.head.value, 2)
        self.assertEqual(self.asc_list.tail.value, 5)
        self.assertEqual(self.asc_list.len(), 2)

    def test_add_asc_in_tail(self):
        self.asc_list.add(5)
        self.asc_list.add(6)

        self.assertEqual(self.asc_list.head.value, 5)
        self.assertEqual(self.asc_list.tail.value, 6)
        self.assertEqual(self.asc_list.len(), 2)

    def test_add_asc_in_middle(self):
        self.asc_list.add(5)
        self.asc_list.add(7)
        self.asc_list.add(6)

        self.assertEqual(self.asc_list.head.value, 5)
        self.assertEqual(self.asc_list.tail.value, 7)
        self.assertEqual(self.asc_list.head.next.value, 6)
        self.assertEqual(self.asc_list.tail.prev.value, 6)
        self.assertEqual(self.asc_list.len(), 3)

    def test_add_asc_random_case1(self):
        values = [1, 4, 5, 6, 7]
        for case in range(10000):
            random.shuffle(values)
            asc_list = main.OrderedList(True)
            for i in range(len(values)):
                asc_list.add(values[i])

            self.assertEqual(asc_list.head.value, 1)
            self.assertEqual(asc_list.tail.value, 7)
            self.assertEqual(asc_list.head.next.value, 4)
            self.assertEqual(asc_list.tail.prev.value, 6)
            self.assertEqual(asc_list.len(), 5)

    def test_add_asc_random_case2(self):
        values = [1, 1, 4, 6, 7]
        for case in range(10000):
            random.shuffle(values)
            asc_list = main.OrderedList(True)
            for i in range(len(values)):
                asc_list.add(values[i])

            self.assertEqual(asc_list.head.value, 1)
            self.assertEqual(asc_list.tail.value, 7)
            self.assertEqual(asc_list.head.next.value, 1)
            self.assertEqual(asc_list.tail.prev.value, 6)
            self.assertEqual(asc_list.len(), 5)

    def test_add_desc_to_empty(self):
        self.desc_list.add(5)

        self.assertEqual(self.desc_list.head.value, 5)
        self.assertEqual(self.desc_list.tail.value, 5)
        self.assertEqual(self.desc_list.len(), 1)

    def test_add_desc_in_head(self):
        self.desc_list.add(2)
        self.desc_list.add(5)

        self.assertEqual(self.desc_list.head.value, 5)
        self.assertEqual(self.desc_list.tail.value, 2)
        self.assertEqual(self.desc_list.len(), 2)

    def test_add_desc_in_tail(self):
        self.desc_list.add(6)
        self.desc_list.add(5)

        self.assertEqual(self.desc_list.head.value, 6)
        self.assertEqual(self.desc_list.tail.value, 5)
        self.assertEqual(self.desc_list.len(), 2)

    def test_add_desc_in_middle(self):
        self.desc_list.add(5)
        self.desc_list.add(7)
        self.desc_list.add(6)

        self.assertEqual(self.desc_list.head.value, 7)
        self.assertEqual(self.desc_list.tail.value, 5)
        self.assertEqual(self.desc_list.head.next.value, 6)
        self.assertEqual(self.desc_list.tail.prev.value, 6)
        self.assertEqual(self.desc_list.len(), 3)

    def test_add_desc_random_case1(self):
        values = [1, 4, 5, 6, 7]
        for case in range(10000):
            random.shuffle(values)
            desc_list = main.OrderedList(False)
            for i in range(len(values)):
                desc_list.add(values[i])

            self.assertEqual(desc_list.head.value, 7)
            self.assertEqual(desc_list.tail.value, 1)
            self.assertEqual(desc_list.head.next.value, 6)
            self.assertEqual(desc_list.tail.prev.value, 4)
            self.assertEqual(desc_list.len(), 5)

    def test_add_desc_random_case2(self):
        values = [1, 1, 4, 6, 7]
        for case in range(10000):
            random.shuffle(values)
            desc_list = main.OrderedList(False)
            for i in range(len(values)):
                desc_list.add(values[i])

            self.assertEqual(desc_list.head.value, 7)
            self.assertEqual(desc_list.tail.value, 1)
            self.assertEqual(desc_list.head.next.value,6)
            self.assertEqual(desc_list.tail.prev.value, 1)
            self.assertEqual(desc_list.len(), 5)

    def test_find_asc_not_exists_full_scan(self):
        self.asc_list.add(1)
        self.asc_list.add(2)
        self.asc_list.add(3)

        self.assertEqual(self.asc_list.find(5), None)

    def test_find_asc_not_exists_part_scan(self):
        self.asc_list.add(1)
        self.asc_list.add(2)
        self.asc_list.add(4)
        self.asc_list.add(5)

        self.assertEqual(self.asc_list.find(3), None)

    def test_find_asc_exists(self):
        self.asc_list.add(1)
        self.asc_list.add(2)
        self.asc_list.add(3)
        self.asc_list.add(4)

        self.assertEqual(self.asc_list.find(2).value, 2)

    def test_find_desc_not_exists_full_scan(self):
        self.desc_list.add(1)
        self.desc_list.add(2)
        self.desc_list.add(3)

        self.assertEqual(self.desc_list.find(0), None)

    def test_find_desc_not_exists_part_scan(self):
        self.desc_list.add(1)
        self.desc_list.add(2)
        self.desc_list.add(4)
        self.desc_list.add(5)

        self.assertEqual(self.asc_list.find(3), None)

    def test_find_desc_exists(self):
        self.desc_list.add(1)
        self.desc_list.add(2)
        self.desc_list.add(3)
        self.desc_list.add(4)

        self.assertEqual(self.desc_list.find(4).value, 4)

    def test_delete_asc_one_node(self):
        self.asc_list.add(1)
        self.asc_list.delete(1)

        self.assertEqual(self.asc_list.head, None)
        self.assertEqual(self.asc_list.tail, None)
        self.assertEqual(self.asc_list.len(), 0)

    def test_delete_asc_head(self):
        self.asc_list.add(1)
        self.asc_list.add(5)
        self.asc_list.delete(1)

        self.assertEqual(self.asc_list.head.value, 5)
        self.assertEqual(self.asc_list.tail.value, 5)
        self.assertEqual(self.asc_list.len(), 1)

    def test_delete_asc_tail(self):
        self.asc_list.add(1)
        self.asc_list.add(5)
        self.asc_list.delete(5)

        self.assertEqual(self.asc_list.head.value, 1)
        self.assertEqual(self.asc_list.tail.value, 1)
        self.assertEqual(self.asc_list.len(), 1)

    def test_delete_asc_middle(self):
        self.asc_list.add(1)
        self.asc_list.add(4)
        self.asc_list.add(5)
        self.asc_list.delete(4)

        self.assertEqual(self.asc_list.head.value, 1)
        self.assertEqual(self.asc_list.tail.value, 5)
        self.assertEqual(self.asc_list.len(), 2)

    def test_delete_desc_one_node(self):
        self.desc_list.add(1)
        self.desc_list.delete(1)

        self.assertEqual(self.desc_list.head, None)
        self.assertEqual(self.desc_list.tail, None)
        self.assertEqual(self.desc_list.len(), 0)

    def test_delete_desc_head(self):
        self.desc_list.add(1)
        self.desc_list.add(5)
        self.desc_list.delete(5)

        self.assertEqual(self.desc_list.head.value, 1)
        self.assertEqual(self.desc_list.tail.value, 1)
        self.assertEqual(self.desc_list.len(), 1)

    def test_delete_desc_tail(self):
        self.desc_list.add(1)
        self.desc_list.add(5)
        self.desc_list.delete(1)

        self.assertEqual(self.desc_list.head.value, 5)
        self.assertEqual(self.desc_list.tail.value, 5)
        self.assertEqual(self.desc_list.len(), 1)

    def test_delete_desc_middle(self):
        self.desc_list.add(1)
        self.desc_list.add(4)
        self.desc_list.add(5)
        self.desc_list.delete(4)

        self.assertEqual(self.desc_list.head.value, 5)
        self.assertEqual(self.desc_list.tail.value, 1)
        self.assertEqual(self.desc_list.len(), 2)


class OrderedStringList(unittest.TestCase):

    def setUp(self):
        self.asc_list = main.OrderedStringList(True)
        self.desc_list = main.OrderedStringList(False)

    def test_compare(self):
        self.assertEqual(self.asc_list.compare('   apple ', ' banana'), -1)
        self.assertEqual(self.asc_list.compare('   apple ', ' apple'), 0)
        self.assertEqual(self.asc_list.compare('   c apple ', '     banana  '), 1)


if __name__ == '__main__':
    unittest.main()
