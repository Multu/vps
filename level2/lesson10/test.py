import random
import unittest
import time


import main


class PowerSet(unittest.TestCase):

    def setUp(self):
        self.power_set = main.PowerSet()
        self.set2 = main.PowerSet()

    def test_put_new_item(self):
        self.power_set.put('123')
        self.power_set.put(44)

        self.assertEqual(self.power_set.get('123'), True)
        self.assertEqual(self.power_set.get(44), True)
        self.assertEqual(self.power_set.size(), 2)

    def test_put_exists_item(self):
        self.power_set.put('123')
        self.power_set.put('123')

        self.assertEqual(self.power_set.get('123'), True)
        self.assertEqual(self.power_set.size(), 1)

    def test_remove_exists_item(self):
        self.power_set.put('test')
        self.power_set.put(18)
        self.power_set.put(56)

        self.assertEqual(self.power_set.remove(18), True)
        self.assertEqual(self.power_set.get(18), False)
        self.assertEqual(self.power_set.size(), 2)

    def test_remove_not_exists_item(self):
        self.power_set.put(1)
        self.power_set.put(5)

        self.assertEqual(self.power_set.remove(15), False)
        self.assertEqual(self.power_set.size(), 2)

    def test_intersection_empty_result_case1(self):
        self.power_set.put(1)
        self.power_set.put(5)
        self.power_set.put(7)

        self.set2.put(2)
        self.set2.put(4)
        self.set2.put(6)

        intersect_set = self.power_set.intersection(self.set2)
        self.assertEqual(intersect_set.size(), 0)

    def test_intersection_empty_result_case2(self):
        self.set2.put(2)
        self.set2.put(4)
        self.set2.put(6)

        intersect_set = self.power_set.intersection(self.set2)
        self.assertEqual(intersect_set.size(), 0)

    def test_intersection_empty_result_case3(self):
        self.power_set.put(1)
        self.power_set.put(5)
        self.power_set.put(7)

        intersect_set = self.power_set.intersection(self.set2)
        self.assertEqual(intersect_set.size(), 0)

    def test_intersection_not_empty_result_case1(self):
        self.power_set.put(1)
        self.power_set.put(5)
        self.power_set.put(7)

        self.set2.put(11)
        self.set2.put(5)
        self.set2.put(8)

        intersect_set = self.power_set.intersection(self.set2)
        self.assertEqual(intersect_set.size(), 1)
        self.assertEqual(intersect_set.get(5), True)

    def test_intersection_not_empty_result_case2(self):
        self.power_set.put(1)
        self.power_set.put(5)
        self.power_set.put(7)

        self.set2.put(1)
        self.set2.put(5)
        self.set2.put(7)

        intersect_set = self.power_set.intersection(self.set2)
        self.assertEqual(intersect_set.size(), 3)
        self.assertEqual(intersect_set.get(1), True)
        self.assertEqual(intersect_set.get(5), True)
        self.assertEqual(intersect_set.get(7), True)

    def test_union_both_sets_not_empty(self):
        self.power_set.put(1)
        self.power_set.put(2)
        self.power_set.put(3)

        self.set2.put('1')
        self.set2.put(2)
        self.set2.put('3')

        union_set = self.power_set.union(self.set2)
        self.assertEqual(union_set.size(), 5)
        self.assertEqual(union_set.get(1), True)
        self.assertEqual(union_set.get(2), True)
        self.assertEqual(union_set.get(3), True)
        self.assertEqual(union_set.get('1'), True)
        self.assertEqual(union_set.get('3'), True)

    def test_union_one_set_empty(self):
        self.power_set.put(1)
        self.power_set.put(2)
        self.power_set.put(3)

        union_set = self.power_set.union(self.set2)
        self.assertEqual(union_set.size(), 3)
        self.assertEqual(union_set.get(1), True)
        self.assertEqual(union_set.get(2), True)
        self.assertEqual(union_set.get(3), True)

    def test_union_both_sets_empty(self):
        union_set = self.power_set.union(self.set2)
        self.assertEqual(union_set.size(), 0)

    def test_difference_not_empty_result(self):
        self.power_set.put(1)
        self.power_set.put(2)
        self.power_set.put(3)

        self.set2.put(1)
        self.set2.put(2)
        self.set2.put(8)
        self.set2.put(5)

        difference_set = self.power_set.difference(self.set2)
        self.assertEqual(difference_set.size(), 1)
        self.assertEqual(difference_set.get(3), True)

    def test_difference_empty_result(self):
        self.power_set.put(1)
        self.power_set.put(2)
        self.power_set.put(3)

        self.set2.put(1)
        self.set2.put(2)
        self.set2.put(3)

        difference_set = self.power_set.difference(self.set2)
        self.assertEqual(difference_set.size(), 0)

    def test_issubset_case1(self):
        self.power_set.put(1)
        self.power_set.put(2)
        self.power_set.put(3)

        self.set2.put(1)

        self.assertEqual(self.power_set.issubset(self.set2), True)

    def test_issubset_case2(self):
        self.power_set.put(1)

        self.set2.put(1)
        self.set2.put(2)
        self.set2.put(3)

        self.assertEqual(self.power_set.issubset(self.set2), False)

    def test_issubset_case2(self):
        self.power_set.put(1)
        self.power_set.put(2)
        self.power_set.put(3)

        self.set2.put(1)
        self.set2.put(5)

        self.assertEqual(self.power_set.issubset(self.set2), False)

    def test_issubset_case2(self):
        self.power_set.put(1)
        self.power_set.put(2)
        self.power_set.put(3)

        self.assertEqual(self.power_set.issubset(self.set2), True)

    def test_speed(self):
        max_items_count = 100000
        set1_items = [random.randint(0, 1000000) for i in range(max_items_count)]
        set2_items = [random.randint(0, 1000000) for i in range(max_items_count)]

        for i in range(max_items_count):
            self.power_set.put(set1_items[i])
            self.set2.put(set2_items[i])

        start = time.time()

        union_set = self.power_set.union(self.set2)
        intersect_set = self.power_set.intersection(self.set2)
        difference_set = self.power_set.difference(self.set2)

        end = time.time()

        self.assertLess(end - start, 1)


if __name__ == '__main__':
    unittest.main()


