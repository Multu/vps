import unittest

import main
import extra


class LinkedList2(unittest.TestCase):

    def setUp(self):
        self.linked_list2 = main.LinkedList2()
        self.node1 = main.Node(1)
        self.node2 = main.Node(2)
        self.node3 = main.Node(3)
        self.node4 = main.Node(4)
        self.node5 = main.Node(5)
        self.node6 = main.Node(5)
        self.node7 = main.Node(3)
        self.node8 = main.Node(3)

    def test_add_in_tail(self):
        self.linked_list2.add_in_tail(self.node1)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.tail, self.node1)

        self.linked_list2.add_in_tail(self.node2)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.tail, self.node2)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.tail.prev, self.node1)

    def test_find(self):
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node2)
        self.linked_list2.add_in_tail(self.node3)

        self.assertEqual(self.linked_list2.find(1), self.node1)
        self.assertEqual(self.linked_list2.find(2), self.node2)
        self.assertEqual(self.linked_list2.find(3), self.node3)
        self.assertEqual(self.linked_list2.find(222), None)

    def test_find_all(self):
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node2)
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node7)

        self.assertEqual(self.linked_list2.find_all(3), [self.node3, self.node7])
        self.assertEqual(self.linked_list2.find_all(2), [self.node2])
        self.assertEqual(self.linked_list2.find_all(222), [])

    def test_remove_first_founded(self):
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node2)
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node4)
        self.linked_list2.add_in_tail(self.node5)
        self.linked_list2.add_in_tail(self.node6)
        self.linked_list2.add_in_tail(self.node7)

        self.linked_list2.delete(1)
        self.assertEqual(self.linked_list2.head, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node7)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node3)

        self.linked_list2.delete(14)
        self.assertEqual(self.linked_list2.head, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node7)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node3)

        self.linked_list2.delete(3)
        self.assertEqual(self.linked_list2.head, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node7)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node4)

        self.linked_list2.delete(3)
        self.assertEqual(self.linked_list2.head, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node6)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node4)
        self.assertEqual(self.linked_list2.tail.prev, self.node5)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.delete(4)
        self.assertEqual(self.linked_list2.head, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node6)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node5)
        self.assertEqual(self.linked_list2.tail.prev, self.node5)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.delete(2)
        self.assertEqual(self.linked_list2.head, self.node5)
        self.assertEqual(self.linked_list2.tail, self.node6)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node6)
        self.assertEqual(self.linked_list2.tail.prev, self.node5)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.delete(5)
        self.assertEqual(self.linked_list2.head, self.node6)
        self.assertEqual(self.linked_list2.tail, self.node6)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, None)
        self.assertEqual(self.linked_list2.tail.prev, None)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.delete(5)
        self.assertEqual(self.linked_list2.head, None)
        self.assertEqual(self.linked_list2.tail, None)

    def test_remove_all_founded_from_empty_list(self):
        self.linked_list2.delete(200, True)
        self.assertEqual(self.linked_list2.head, None)
        self.assertEqual(self.linked_list2.tail, None)

    def test_remove_all_founded_from_one_size_list(self):
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.delete(1, True)
        self.assertEqual(self.linked_list2.head, None)
        self.assertEqual(self.linked_list2.tail, None)

    def test_remove_all_founded_from_head_position_case_1(self):
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node2)
        self.linked_list2.delete(1, True)
        self.assertEqual(self.linked_list2.head, self.node2)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, None)
        self.assertEqual(self.linked_list2.tail, self.node2)
        self.assertEqual(self.linked_list2.tail.prev, None)
        self.assertEqual(self.linked_list2.tail.next, None)

    def test_remove_all_founded_from_head_position_case_2(self):
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node7)
        self.linked_list2.delete(3, True)
        self.assertEqual(self.linked_list2.head, None)
        self.assertEqual(self.linked_list2.tail, None)

    def test_remove_all_founded_from_head_position_case_3(self):
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node7)
        self.linked_list2.add_in_tail(self.node6)
        self.linked_list2.delete(3, True)
        self.assertEqual(self.linked_list2.head, self.node6)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, None)
        self.assertEqual(self.linked_list2.tail, self.node6)
        self.assertEqual(self.linked_list2.tail.prev, None)
        self.assertEqual(self.linked_list2.tail.next, None)

    def test_remove_all_founded_from_head_position_case_4(self):
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node7)
        self.linked_list2.add_in_tail(self.node6)
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.delete(3, True)
        self.assertEqual(self.linked_list2.head, self.node6)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node1)
        self.assertEqual(self.linked_list2.tail, self.node1)
        self.assertEqual(self.linked_list2.tail.prev, self.node6)
        self.assertEqual(self.linked_list2.tail.next, None)

    def test_remove_all_founded_from_tail_position_case_1(self):
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node6)
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node7)
        self.linked_list2.delete(3, True)
        self.assertEqual(self.linked_list2.head, self.node6)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node1)
        self.assertEqual(self.linked_list2.tail, self.node1)
        self.assertEqual(self.linked_list2.tail.prev, self.node6)
        self.assertEqual(self.linked_list2.tail.next, None)

    def test_remove_all_founded_from_tail_position_case_2(self):
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node2)
        self.linked_list2.add_in_tail(self.node7)
        self.linked_list2.add_in_tail(self.node8)
        self.linked_list2.delete(3, True)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node2)
        self.assertEqual(self.linked_list2.tail.prev, self.node1)
        self.assertEqual(self.linked_list2.tail.next, None)

    def test_remove_all_founded_from_tail_position_case_3(self):
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node7)
        self.linked_list2.add_in_tail(self.node8)
        self.linked_list2.delete(3, True)
        self.assertEqual(self.linked_list2.head, None)
        self.assertEqual(self.linked_list2.tail, None)

    def test_remove_all_founded_from_middle_position(self):
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node2)
        self.linked_list2.add_in_tail(self.node7)
        self.linked_list2.add_in_tail(self.node8)
        self.linked_list2.add_in_tail(self.node4)
        self.linked_list2.add_in_tail(self.node5)
        self.linked_list2.delete(3, True)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node5)
        self.assertEqual(self.linked_list2.tail.prev, self.node4)
        self.assertEqual(self.linked_list2.tail.next, None)

    def test_len(self):
        self.assertEqual(self.linked_list2.len(), 0)

        self.linked_list2.add_in_tail(self.node6)
        self.assertEqual(self.linked_list2.len(), 1)

        self.linked_list2.add_in_tail(self.node4)
        self.assertEqual(self.linked_list2.len(), 2)

    def test_clean(self):
        self.linked_list2.add_in_tail(self.node1)
        self.linked_list2.add_in_tail(self.node2)
        self.linked_list2.add_in_tail(self.node3)
        self.linked_list2.clean()
        self.assertEqual(self.linked_list2.head, None)
        self.assertEqual(self.linked_list2.tail, None)

    def test_add_in_head(self):
        self.linked_list2.add_in_head(self.node1)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, None)
        self.assertEqual(self.linked_list2.tail, self.node1)
        self.assertEqual(self.linked_list2.tail.prev, None)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.add_in_head(self.node2)
        self.assertEqual(self.linked_list2.head, self.node2)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node1)
        self.assertEqual(self.linked_list2.tail, self.node1)
        self.assertEqual(self.linked_list2.tail.prev, self.node2)
        self.assertEqual(self.linked_list2.tail.next, None)

    def test_insert(self):
        self.linked_list2.insert(self.node1, self.node2)
        self.assertEqual(self.linked_list2.head, None)
        self.assertEqual(self.linked_list2.tail, None)

        self.linked_list2.insert(None, self.node1)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, None)
        self.assertEqual(self.linked_list2.tail, self.node1)
        self.assertEqual(self.linked_list2.tail.prev, None)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.insert(self.node1, self.node2)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node2)
        self.assertEqual(self.linked_list2.tail, self.node2)
        self.assertEqual(self.linked_list2.tail.prev, self.node1)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.insert(self.node1, self.node3)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node3)
        self.assertEqual(self.linked_list2.tail, self.node2)
        self.assertEqual(self.linked_list2.tail.prev, self.node3)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.insert(None, self.node4)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node3)
        self.assertEqual(self.linked_list2.tail, self.node4)
        self.assertEqual(self.linked_list2.tail.prev, self.node2)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.insert(self.node6, self.node5)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node3)
        self.assertEqual(self.linked_list2.tail, self.node4)
        self.assertEqual(self.linked_list2.tail.prev, self.node2)
        self.assertEqual(self.linked_list2.tail.next, None)

        self.linked_list2.insert(self.node2, self.node5)
        self.assertEqual(self.linked_list2.head, self.node1)
        self.assertEqual(self.linked_list2.head.prev, None)
        self.assertEqual(self.linked_list2.head.next, self.node3)
        self.assertEqual(self.linked_list2.tail, self.node4)
        self.assertEqual(self.linked_list2.tail.prev, self.node5)
        self.assertEqual(self.linked_list2.tail.next, None)


if __name__ == '__main__':
    unittest.main()
