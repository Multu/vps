import unittest

import main


class SimpleTree(unittest.TestCase):

    def setUp(self):
        # Empty tree.
        self.empty_tree = main.SimpleTree(None)

        # Full tree, see photo from readme file.
        node_level1 = main.SimpleTreeNode(9, None)

        node_level2_1 = main.SimpleTreeNode(4, node_level1)
        node_level2_2 = main.SimpleTreeNode(17, node_level1)
        node_level1.Children.append(node_level2_1)
        node_level1.Children.append(node_level2_2)

        node_level3_1 = main.SimpleTreeNode(3, node_level2_1)
        node_level3_2 = main.SimpleTreeNode(6, node_level2_1)
        node_level2_1.Children.append(node_level3_1)
        node_level2_1.Children.append(node_level3_2)

        node_level3_3 = main.SimpleTreeNode(22, node_level2_2)
        node_level2_2.Children.append(node_level3_3)

        node_level4_1 = main.SimpleTreeNode(5, node_level3_2)
        node_level4_2 = main.SimpleTreeNode(7, node_level3_2)
        node_level3_2.Children.append(node_level4_1)
        node_level3_2.Children.append(node_level4_2)

        node_level4_3 = main.SimpleTreeNode(20, node_level3_3)
        node_level3_3.Children.append(node_level4_3)

        self.full_tree = main.SimpleTree(node_level1)

    def test_add_child_to_empty_tree(self):
        new_node = main.SimpleTreeNode(99, None)
        self.empty_tree.AddChild(None, new_node)

        self.assertEqual(self.empty_tree.Root, new_node)
        self.assertEqual(len(self.empty_tree.Root.Children), 0)

    def test_add_child_to_full_tree_to_middle_place(self):
        parent_node = self.full_tree.Root.Children[0].Children[1]  # node with value 6
        new_node = main.SimpleTreeNode(99, None)
        self.full_tree.AddChild(parent_node, new_node)

        self.assertEqual(len(parent_node.Children), 3)
        self.assertEqual(parent_node.Children[2], new_node)

    def test_delete_node(self):
        node_to_delete = self.full_tree.Root.Children[0].Children[1]  # node with value 6
        self.full_tree.DeleteNode(node_to_delete)

        self.assertEqual(len(self.full_tree.Root.Children[0].Children), 1)
        self.assertEqual(self.full_tree.Root.Children[0].Children[0].NodeValue, 3)

    def test_get_all_nodes(self):
        all_nodes = self.full_tree.GetAllNodes()
        all_nodes_values = []
        for node in all_nodes:
            all_nodes_values.append(node.NodeValue)

        self.assertEqual(len(all_nodes_values), 9)
        self.assertEqual(all_nodes_values, [9, 4, 17, 3, 6, 22, 5, 7, 20])

        all_nodes = self.empty_tree.GetAllNodes()
        self.assertEqual(len(all_nodes), 0)

    def test_find_nodes_by_value(self):
        found_nodes = self.full_tree.FindNodesByValue(13)
        self.assertEqual(len(found_nodes), 0)

        found_nodes = self.full_tree.FindNodesByValue(17)
        found_nodes_values = []
        for node in found_nodes:
            found_nodes_values.append(node.NodeValue)
        self.assertEqual(found_nodes_values, [17])

    def test_move_node(self):
        original_node = self.full_tree.Root.Children[0].Children[1]  # node with value 6
        new_parent_node = self.full_tree.Root.Children[1].Children[0]  # node with value 22

        self.full_tree.MoveNode(original_node, new_parent_node)

        self.assertEqual(len(self.full_tree.Root.Children[0].Children), 1)
        self.assertEqual(self.full_tree.Root.Children[0].Children[0].NodeValue, 3)

        self.assertEqual(len(self.full_tree.Root.Children[1].Children[0].Children), 2)
        self.assertEqual(self.full_tree.Root.Children[1].Children[0].Children[0].NodeValue, 20)
        self.assertEqual(self.full_tree.Root.Children[1].Children[0].Children[1].NodeValue, 6)

    def test_count(self):
        self.assertEqual(self.empty_tree.Count(), 0)
        self.assertEqual(self.full_tree.Count(), 9)

    def test_count(self):
        self.assertEqual(self.empty_tree.LeafCount(), 0)
        self.assertEqual(self.full_tree.LeafCount(), 4)

    def test_set_levels(self):
        self.full_tree.SetLevels()

        self.assertEqual(self.full_tree.Root.Level, 0)
        self.assertEqual(self.full_tree.Root.Children[0].Level, 1)
        self.assertEqual(self.full_tree.Root.Children[1].Level, 1)
        self.assertEqual(self.full_tree.Root.Children[0].Children[0].Level, 2)
        self.assertEqual(self.full_tree.Root.Children[0].Children[1].Level, 2)
        self.assertEqual(self.full_tree.Root.Children[1].Children[0].Level, 2)
        self.assertEqual(self.full_tree.Root.Children[0].Children[1].Children[0].Level, 3)
        self.assertEqual(self.full_tree.Root.Children[0].Children[1].Children[1].Level, 3)
        self.assertEqual(self.full_tree.Root.Children[1].Children[0].Children[0].Level, 3)


if __name__ == '__main__':
    unittest.main()
