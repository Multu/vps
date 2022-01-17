import unittest
import random

import main


class SimpleTree(unittest.TestCase):

    def setUp(self):
        # Empty tree.
        self.empty_tree = main.SimpleTree(None)


        # Odd tree.
        node_level1 = main.SimpleTreeNode(1, None)

        node_level2_1 = main.SimpleTreeNode(2, node_level1)
        node_level2_2 = main.SimpleTreeNode(3, node_level1)
        node_level1.Children.append(node_level2_1)
        node_level1.Children.append(node_level2_2)

        self.odd_tree = main.SimpleTree(node_level1)


        # Full tree, see photo from readme file.
        node_level1 = main.SimpleTreeNode(1, None)

        node_level2_1 = main.SimpleTreeNode(2, node_level1)
        node_level2_2 = main.SimpleTreeNode(3, node_level1)
        node_level2_3 = main.SimpleTreeNode(6, node_level1)
        node_level1.Children.append(node_level2_1)
        node_level1.Children.append(node_level2_2)
        node_level1.Children.append(node_level2_3)

        node_level3_1 = main.SimpleTreeNode(5, node_level2_1)
        node_level3_2 = main.SimpleTreeNode(7, node_level2_1)
        node_level3_3 = main.SimpleTreeNode(4, node_level2_2)
        node_level3_4 = main.SimpleTreeNode(8, node_level2_3)
        node_level2_1.Children.append(node_level3_1)
        node_level2_1.Children.append(node_level3_2)
        node_level2_2.Children.append(node_level3_3)
        node_level2_3.Children.append(node_level3_4)

        node_level4_1 = main.SimpleTreeNode(9, node_level3_4)
        node_level4_2 = main.SimpleTreeNode(10, node_level3_4)
        node_level3_4.Children.append(node_level4_1)
        node_level3_4.Children.append(node_level4_2)

        self.full_tree = main.SimpleTree(node_level1)

    def test_even_trees_empty(self):
        self.assertEqual(self.empty_tree.EvenTrees(), [])

    def test_even_trees_odd(self):
        self.assertEqual(self.empty_tree.EvenTrees(), [])

    def test_even_trees_full(self):
        even_nodes = self.full_tree.EvenTrees()

        even_nodes_values = []
        for node in even_nodes:
            even_nodes_values.append(node.NodeValue)

        self.assertEqual(even_nodes_values, [1, 3, 1, 6])

if __name__ == '__main__':
    unittest.main()
