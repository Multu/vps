import unittest

import main
import extra


class LinkedList(unittest.TestCase):

    def test_add_in_tail(self):
        l_list = main.LinkedList()
        n1 = main.Node(12)
        n2 = main.Node(55)
        n3 = main.Node(128)
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)

        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail.value, 128)

    def test_find(self):
        l_list = main.LinkedList()
        n1 = main.Node(12)
        n2 = main.Node(55)
        n3 = main.Node(128)
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)

        self.assertEqual(l_list.find(55), n2)
        self.assertEqual(l_list.find(12), n1)
        self.assertEqual(l_list.find(128), n3)
        self.assertEqual(l_list.find(333), None)

    def test_find_all(self):
        l_list = main.LinkedList()
        n1 = main.Node(12)
        n2 = main.Node(55)
        n3 = main.Node(128)
        n4 = main.Node(12)

        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.add_in_tail(n4)

        self.assertEqual(l_list.find_all(55), [n2])
        self.assertEqual(l_list.find_all(12), [n1, n4])
        self.assertEqual(l_list.find_all(128), [n3])
        self.assertEqual(l_list.find_all(333), [])

    def test_remove_first_from_empty(self):
        l_list = main.LinkedList()
        l_list.delete(5)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    def test_remove_first_from_one_size(self):
        n1 = main.Node(5)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.delete(5)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    def test_remove_first_from_head_position(self):
        n1 = main.Node(5)
        n2 = main.Node(7)
        n3 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.delete(5)
        self.assertEqual(l_list.head, n2)
        self.assertEqual(l_list.tail, n2)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.delete(5)
        self.assertEqual(l_list.head, n2)
        self.assertEqual(l_list.tail, n3)

    def test_remove_first_from_tail_position(self):
        n1 = main.Node(5)
        n2 = main.Node(7)
        n3 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.delete(7)
        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n1)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.delete(9)
        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n2)

    def test_remove_first_from_middle_position(self):
        n1 = main.Node(5)
        n2 = main.Node(7)
        n3 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.delete(7)
        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n3)

    def test_remove_first_not_found(self):
        n1 = main.Node(5)
        n2 = main.Node(7)
        n3 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.delete(34)

        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n3)

    def test_remove_all_from_empty(self):
        l_list = main.LinkedList()
        l_list.delete(5, True)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    def test_remove_all_from_one_size(self):
        n1 = main.Node(5)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.delete(5, True)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    def test_remove_all_from_head_position(self):
        n1 = main.Node(5)
        n2 = main.Node(7)
        n3 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.delete(5, True)
        self.assertEqual(l_list.head, n2)
        self.assertEqual(l_list.tail, n2)

        n1 = main.Node(5)
        n2 = main.Node(5)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.delete(5, True)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

        n1 = main.Node(5)
        n2 = main.Node(5)
        n3 = main.Node(7)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.delete(5, True)
        self.assertEqual(l_list.head, n3)
        self.assertEqual(l_list.tail, n3)

        n1 = main.Node(5)
        n2 = main.Node(5)
        n3 = main.Node(7)
        n4 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.add_in_tail(n4)
        l_list.delete(5, True)
        self.assertEqual(l_list.head, n3)
        self.assertEqual(l_list.tail, n4)

    def test_remove_all_from_tail_position(self):
        n1 = main.Node(9)
        n2 = main.Node(7)
        n3 = main.Node(5)
        n4 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.add_in_tail(n4)
        l_list.delete(9, True)
        self.assertEqual(l_list.head, n2)
        self.assertEqual(l_list.tail, n3)

        n1 = main.Node(5)
        n2 = main.Node(9)
        n3 = main.Node(5)
        n4 = main.Node(9)
        n5 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.add_in_tail(n4)
        l_list.add_in_tail(n5)
        l_list.delete(9, True)
        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n3)

        n1 = main.Node(9)
        n2 = main.Node(9)
        n3 = main.Node(9)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.delete(9, True)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    def test_remove_all_from_middle_position(self):
        n1 = main.Node(1)
        n2 = main.Node(2)
        n3 = main.Node(3)
        n4 = main.Node(1)
        n5 = main.Node(1)
        n6 = main.Node(1)
        n7 = main.Node(1)
        n8 = main.Node(2)
        n9 = main.Node(3)

        l_list = main.LinkedList()
        l_list.add_in_tail(n1)
        l_list.add_in_tail(n2)
        l_list.add_in_tail(n3)
        l_list.add_in_tail(n4)
        l_list.add_in_tail(n5)
        l_list.add_in_tail(n6)
        l_list.add_in_tail(n7)
        l_list.add_in_tail(n8)
        l_list.add_in_tail(n9)
        l_list.delete(1, True)
        self.assertEqual(l_list.head, n2)
        self.assertEqual(l_list.tail, n9)
        self.assertEqual(l_list.len(), 4)

    def test_len(self):
        l_list = main.LinkedList()
        self.assertEqual(l_list.len(), 0)

        l_list = main.LinkedList()
        l_list.add_in_tail(main.Node(4))
        self.assertEqual(l_list.len(), 1)

        l_list = main.LinkedList()
        l_list.add_in_tail(main.Node(4))
        l_list.add_in_tail(main.Node(4))
        self.assertEqual(l_list.len(), 2)

    def test_clean(self):
        l_list = main.LinkedList()
        l_list.add_in_tail(main.Node(1))
        l_list.add_in_tail(main.Node(2))
        l_list.add_in_tail(main.Node(3))
        l_list.clean()

        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

    def test_insert(self):
        n1 = main.Node(1)
        n2 = main.Node(2)
        n3 = main.Node(3)
        n4 = main.Node(4)
        n5 = main.Node(5)
        l_list = main.LinkedList()

        l_list.insert(n2, n1)
        self.assertEqual(l_list.head, None)
        self.assertEqual(l_list.tail, None)

        l_list.insert(None, n1)
        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n1)

        l_list.insert(n1, n2)
        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n2)

        l_list.insert(n1, n3)
        self.assertEqual(l_list.head, n1)
        self.assertEqual(l_list.tail, n2)

        l_list.insert(None, n4)
        self.assertEqual(l_list.head, n4)
        self.assertEqual(l_list.tail, n2)

        l_list.insert(main.Node(2), n5)
        self.assertEqual(l_list.head, n4)
        self.assertEqual(l_list.tail, n2)

        l_list.insert(n2, n5)
        self.assertEqual(l_list.head, n4)
        self.assertEqual(l_list.tail, n5)


class LinkedListExtra(unittest.TestCase):
    def test_sum_same_linked_lists(self):
        list_a = main.LinkedList()
        list_a.add_in_tail(main.Node(3))
        list_a.add_in_tail(main.Node(5))
        list_a.add_in_tail(main.Node(2))

        list_b = main.LinkedList()
        list_b.add_in_tail(main.Node(9))
        list_b.add_in_tail(main.Node(2))
        list_b.add_in_tail(main.Node(1))

        correct_result = [12, 7, 3]

        sum_list = extra.sum_linked_lists(list_a, list_b)
        test_result = []
        head = sum_list.head
        while head is not None:
            test_result.append(head.value)
            head = head.next

        self.assertEqual(test_result, correct_result)

    def test_sum_diff_linked_lists(self):
        list_a = main.LinkedList()
        list_a.add_in_tail(main.Node(9))
        list_a.add_in_tail(main.Node(9))

        list_b = main.LinkedList()
        list_b.add_in_tail(main.Node(9))
        list_b.add_in_tail(main.Node(9))
        list_b.add_in_tail(main.Node(9))

        sum_list = extra.sum_linked_lists(list_a, list_b)
        self.assertEqual(sum_list.head, None)


if __name__ == '__main__':
    unittest.main()
