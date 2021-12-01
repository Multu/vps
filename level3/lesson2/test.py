import unittest

import main


class BinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.empty_tree = main.BST(None)

        """
            Full tree. Example below:
                             8
                     4              12
                2        6      10       14
        """
        node_root = main.BSTNode(8, 8, None)

        node_level1_1 = main.BSTNode(4, 4, node_root)
        node_level1_2 = main.BSTNode(12, 12, node_root)
        node_root.LeftChild = node_level1_1
        node_root.RightChild = node_level1_2

        node_level2_1 = main.BSTNode(2, 2, node_level1_1)
        node_level2_2 = main.BSTNode(6, 6, node_level1_1)
        node_level2_3 = main.BSTNode(10, 10, node_level1_2)
        node_level2_4 = main.BSTNode(14, 14, node_level1_2)
        node_level1_1.LeftChild = node_level2_1
        node_level1_1.RightChild = node_level2_2
        node_level1_2.LeftChild = node_level2_3
        node_level1_2.RightChild = node_level2_4

        self.full_tree = main.BST(node_root)

    def test_find_node_by_key(self):
        # Find in empty tree.
        founded_node = self.empty_tree.FindNodeByKey(100)
        self.assertEqual(founded_node.Node, None)

        # Find not exists key. Will be added to the left child place.
        founded_node = self.full_tree.FindNodeByKey(5)
        self.assertEqual(founded_node.Node.NodeKey, 6)
        self.assertEqual(founded_node.NodeHasKey, False)
        self.assertEqual(founded_node.ToLeft, True)

        # Find not exists key. Will be added to the right child place.
        founded_node = self.full_tree.FindNodeByKey(15)
        self.assertEqual(founded_node.Node.NodeKey, 14)
        self.assertEqual(founded_node.NodeHasKey, False)
        self.assertEqual(founded_node.ToLeft, False)

        # Find exists key.
        founded_node = self.full_tree.FindNodeByKey(12)
        self.assertEqual(founded_node.Node.NodeKey, 12)
        self.assertEqual(founded_node.NodeHasKey, True)
        self.assertEqual(founded_node.ToLeft, False)

    def test_add_key_value(self):
        # Add new node as left child.
        self.assertEqual(self.full_tree.FindNodeByKey(5).NodeHasKey, False)
        self.assertEqual(self.full_tree.AddKeyValue(5, 5), True)
        self.assertEqual(self.full_tree.FindNodeByKey(5).NodeHasKey, True)

        # Add new node as right child.
        self.assertEqual(self.full_tree.FindNodeByKey(7).NodeHasKey, False)
        self.assertEqual(self.full_tree.AddKeyValue(7, 7), True)
        self.assertEqual(self.full_tree.FindNodeByKey(7).NodeHasKey, True)

        # Add duplicated node.
        self.assertEqual(self.full_tree.FindNodeByKey(4).NodeHasKey, True)
        self.assertEqual(self.full_tree.AddKeyValue(4, 4), False)
        self.assertEqual(self.full_tree.FindNodeByKey(4).NodeHasKey, True)

    def test_find_min_max(self):
        root = self.full_tree.Root
        from_node = self.full_tree.FindNodeByKey(12).Node
        leaf_node = self.full_tree.FindNodeByKey(6).Node

        self.assertEqual(self.full_tree.FinMinMax(root, False).NodeKey, 2)
        self.assertEqual(self.full_tree.FinMinMax(root, True).NodeKey, 14)
        self.assertEqual(self.full_tree.FinMinMax(from_node, False).NodeKey, 10)
        self.assertEqual(self.full_tree.FinMinMax(from_node, True).NodeKey, 14)
        self.assertEqual(self.full_tree.FinMinMax(leaf_node, False).NodeKey, 6)
        self.assertEqual(self.full_tree.FinMinMax(leaf_node, True).NodeKey, 6)

    def test_delete_node_by_key_root_element(self):
        self.assertEqual(self.full_tree.FindNodeByKey(8).NodeHasKey, True)
        self.assertEqual(self.full_tree.DeleteNodeByKey(8), True)
        self.assertEqual(self.full_tree.FindNodeByKey(8).NodeHasKey, False)

        self.assertEqual(self.full_tree.Root.NodeKey, 10)
        self.assertEqual(self.full_tree.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.full_tree.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.full_tree.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(self.full_tree.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(self.full_tree.Root.RightChild.LeftChild, None)
        self.assertEqual(self.full_tree.Root.RightChild.RightChild.NodeKey, 14)

    def test_delete_node_by_key_not_existing(self):
        self.assertEqual(self.full_tree.FindNodeByKey(33).NodeHasKey, False)
        self.assertEqual(self.full_tree.DeleteNodeByKey(33), False)
        self.assertEqual(self.full_tree.FindNodeByKey(33).NodeHasKey, False)

    def test_delete_node_by_key_one_element_in_tree(self):
        self.empty_tree.AddKeyValue(4, 4)

        self.assertEqual(self.empty_tree.FindNodeByKey(4).NodeHasKey, True)
        self.assertEqual(self.empty_tree.DeleteNodeByKey(4), True)
        self.assertEqual(self.empty_tree.FindNodeByKey(4).NodeHasKey, False)

    def test_delete_node_by_key_left_leaf(self):
        self.assertEqual(self.full_tree.FindNodeByKey(2).NodeHasKey, True)
        self.assertEqual(self.full_tree.DeleteNodeByKey(2), True)
        self.assertEqual(self.full_tree.FindNodeByKey(2).NodeHasKey, False)

        self.assertEqual(self.full_tree.Root.NodeKey, 8)
        self.assertEqual(self.full_tree.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.full_tree.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.full_tree.Root.LeftChild.LeftChild, None)
        self.assertEqual(self.full_tree.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(self.full_tree.Root.RightChild.LeftChild.NodeKey, 10)
        self.assertEqual(self.full_tree.Root.RightChild.RightChild.NodeKey, 14)

    def test_delete_node_by_key_right_leaf(self):
        self.assertEqual(self.full_tree.FindNodeByKey(6).NodeHasKey, True)
        self.assertEqual(self.full_tree.DeleteNodeByKey(6), True)
        self.assertEqual(self.full_tree.FindNodeByKey(6).NodeHasKey, False)

        self.assertEqual(self.full_tree.Root.NodeKey, 8)
        self.assertEqual(self.full_tree.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.full_tree.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.full_tree.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(self.full_tree.Root.LeftChild.RightChild, None)
        self.assertEqual(self.full_tree.Root.RightChild.LeftChild.NodeKey, 10)
        self.assertEqual(self.full_tree.Root.RightChild.RightChild.NodeKey, 14)

    def test_delete_node_by_key_case1(self):
        self.empty_tree.AddKeyValue(4, 4)
        self.empty_tree.AddKeyValue(6, 6)
        self.empty_tree.AddKeyValue(5, 5)
        self.empty_tree.AddKeyValue(7, 7)
        self.empty_tree.AddKeyValue(9, 9)

        self.assertEqual(self.empty_tree.FindNodeByKey(6).NodeHasKey, True)
        self.assertEqual(self.empty_tree.DeleteNodeByKey(6), True)
        self.assertEqual(self.empty_tree.FindNodeByKey(6).NodeHasKey, False)

        self.assertEqual(self.empty_tree.Root.NodeKey, 4)
        self.assertEqual(self.empty_tree.Root.LeftChild, None)
        self.assertEqual(self.empty_tree.Root.RightChild.NodeKey, 7)
        self.assertEqual(self.empty_tree.Root.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(self.empty_tree.Root.RightChild.RightChild.NodeKey, 9)

    def test_delete_node_by_key_case1(self):
        self.empty_tree.AddKeyValue(5, 5)
        self.empty_tree.AddKeyValue(2, 2)
        self.empty_tree.AddKeyValue(16, 16)
        self.empty_tree.AddKeyValue(6, 6)
        self.empty_tree.AddKeyValue(20, 20)
        self.empty_tree.AddKeyValue(17, 17)
        self.empty_tree.AddKeyValue(30, 30)
        self.empty_tree.AddKeyValue(19, 19)
        self.empty_tree.AddKeyValue(18, 18)

        self.assertEqual(self.empty_tree.FindNodeByKey(16).NodeHasKey, True)
        self.assertEqual(self.empty_tree.DeleteNodeByKey(16), True)
        self.assertEqual(self.empty_tree.FindNodeByKey(16).NodeHasKey, False)

        self.assertEqual(self.empty_tree.Root.NodeKey, 5)
        self.assertEqual(self.empty_tree.Root.LeftChild.NodeKey, 2)
        self.assertEqual(self.empty_tree.Root.RightChild.NodeKey, 17)
        self.assertEqual(self.empty_tree.Root.RightChild.LeftChild.NodeKey, 6)
        self.assertEqual(self.empty_tree.Root.RightChild.RightChild.NodeKey, 20)
        self.assertEqual(self.empty_tree.Root.RightChild.RightChild.LeftChild.NodeKey, 19)
        self.assertEqual(self.empty_tree.Root.RightChild.RightChild.RightChild.NodeKey, 30)
        self.assertEqual(self.empty_tree.Root.RightChild.RightChild.LeftChild.LeftChild.NodeKey, 18)

    def test_count(self):
        self.assertEqual(self.full_tree.Count(), 7)
        self.assertEqual(self.empty_tree.Count(), 0)

    def test_count_case1(self):
        self.empty_tree.AddKeyValue(5, 5)
        self.empty_tree.AddKeyValue(2, 2)
        self.empty_tree.AddKeyValue(16, 16)
        self.empty_tree.AddKeyValue(6, 6)
        self.empty_tree.AddKeyValue(20, 20)
        self.empty_tree.AddKeyValue(17, 17)
        self.empty_tree.AddKeyValue(30, 30)
        self.empty_tree.AddKeyValue(19, 19)
        self.empty_tree.AddKeyValue(18, 18)

        self.assertEqual(self.empty_tree.Count(), 9)


if __name__ == '__main__':
    unittest.main()
