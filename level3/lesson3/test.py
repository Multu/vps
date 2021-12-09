import unittest

import main


class BinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.empty_tree = main.BST(None)

        """
            Full tree. Example below:
                             10
                     5              15
                3        7      12       18
              1   4                   16
        """
        node_root = main.BSTNode(10, 10, None)

        node_level1_1 = main.BSTNode(5, 5, node_root)
        node_level1_2 = main.BSTNode(15, 15, node_root)
        node_root.LeftChild = node_level1_1
        node_root.RightChild = node_level1_2

        node_level2_1 = main.BSTNode(3, 3, node_level1_1)
        node_level2_2 = main.BSTNode(7, 7, node_level1_1)
        node_level2_3 = main.BSTNode(12, 12, node_level1_2)
        node_level2_4 = main.BSTNode(18, 18, node_level1_2)
        node_level1_1.LeftChild = node_level2_1
        node_level1_1.RightChild = node_level2_2
        node_level1_2.LeftChild = node_level2_3
        node_level1_2.RightChild = node_level2_4

        node_level3_1 = main.BSTNode(1, 1, node_level2_1)
        node_level3_2 = main.BSTNode(4, 4, node_level2_1)
        node_level3_3 = main.BSTNode(16, 16, node_level2_4)
        node_level2_1.LeftChild = node_level3_1
        node_level2_1.RightChild = node_level3_2
        node_level2_4.LeftChild = node_level3_3

        self.full_tree = main.BST(node_root)

    def test_deep_all_nodes_pre_order(self):
        all_nodes = self.full_tree.DeepAllNodes(2)
        all_values = []
        for node in all_nodes:
            all_values.append(node.NodeValue)

        self.assertEqual(all_values, [10, 5, 3, 1, 4, 7, 15, 12, 18, 16])

    def test_deep_all_nodes_in_order(self):
        all_nodes = self.full_tree.DeepAllNodes(0)
        all_values = []
        for node in all_nodes:
            all_values.append(node.NodeValue)

        self.assertEqual(all_values, [1, 3, 4, 5, 7, 10, 12, 15, 16, 18])

    def test_deep_all_nodes_post_order(self):
        all_nodes = self.full_tree.DeepAllNodes(1)
        all_values = []
        for node in all_nodes:
            all_values.append(node.NodeValue)

        self.assertEqual(all_values, [1, 4, 3, 7, 5, 12, 16, 18, 15, 10])

    def test_wide_all_nodes(self):
        all_nodes = self.full_tree.WideAllNodes()
        all_values = []
        for node in all_nodes:
            all_values.append(node.NodeValue)

        self.assertEqual(all_values, [10, 5, 15, 3, 7, 12, 18, 1, 4, 16])

if __name__ == '__main__':
    unittest.main()
