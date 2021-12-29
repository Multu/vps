import unittest
import random

import main


class BalancedBST(unittest.TestCase):

    def setUp(self):
        self.bbst = main.BalancedBST()

    def test_generate_tree_height_0(self):
        self.bbst.GenerateTree([1])

        self.assertEqual(self.bbst.Root.NodeKey, 1)
        self.assertEqual(self.bbst.Root.Parent, None)
        self.assertEqual(self.bbst.Root.LeftChild, None)
        self.assertEqual(self.bbst.Root.RightChild, None)
        self.assertEqual(self.bbst.Root.Level, 0)

    def test_generate_tree_height_1(self):
        self.bbst.GenerateTree([3, 1, 2])

        root = self.bbst.Root
        root_1 = root.LeftChild
        root_2 = root.RightChild

        self.assertEqual(root.NodeKey, 2)
        self.assertEqual(root.Parent, None)
        self.assertEqual(root.LeftChild, root_1)
        self.assertEqual(root.RightChild, root_2)
        self.assertEqual(root.Level, 0)

        self.assertEqual(root_1.NodeKey, 1)
        self.assertEqual(root_1.Parent, root)
        self.assertEqual(root_1.LeftChild, None)
        self.assertEqual(root_1.RightChild, None)
        self.assertEqual(root_1.Level, 1)

        self.assertEqual(root_2.NodeKey, 3)
        self.assertEqual(root_2.Parent, root)
        self.assertEqual(root_2.LeftChild, None)
        self.assertEqual(root_2.RightChild, None)
        self.assertEqual(root_2.Level, 1)


    def test_generate_tree_height_2(self):
        self.bbst.GenerateTree([7, 6, 5, 4, 3, 2, 1])

        root = self.bbst.Root
        root_1 = root.LeftChild
        root_2 = root.RightChild
        root_1_1 = root_1.LeftChild
        root_1_2 = root_1.RightChild
        root_2_1 = root_2.LeftChild
        root_2_2 = root_2.RightChild

        self.assertEqual(root.NodeKey, 4)
        self.assertEqual(root.Parent, None)
        self.assertEqual(root.LeftChild, root_1)
        self.assertEqual(root.RightChild, root_2)
        self.assertEqual(root.Level, 0)

        self.assertEqual(root_1.NodeKey, 2)
        self.assertEqual(root_1.Parent, root)
        self.assertEqual(root_1.LeftChild, root_1_1)
        self.assertEqual(root_1.RightChild, root_1_2)
        self.assertEqual(root_1.Level, 1)

        self.assertEqual(root_2.NodeKey, 6)
        self.assertEqual(root_2.Parent, root)
        self.assertEqual(root_2.LeftChild, root_2_1)
        self.assertEqual(root_2.RightChild, root_2_2)
        self.assertEqual(root_2.Level, 1)

        self.assertEqual(root_1_1.NodeKey, 1)
        self.assertEqual(root_1_1.Parent, root_1)
        self.assertEqual(root_1_1.LeftChild, None)
        self.assertEqual(root_1_1.RightChild, None)
        self.assertEqual(root_1_1.Level, 2)

        self.assertEqual(root_1_2.NodeKey, 3)
        self.assertEqual(root_1_2.Parent, root_1)
        self.assertEqual(root_1_2.LeftChild, None)
        self.assertEqual(root_1_2.RightChild, None)
        self.assertEqual(root_1_2.Level, 2)

        self.assertEqual(root_2_1.NodeKey, 5)
        self.assertEqual(root_2_1.Parent, root_2)
        self.assertEqual(root_2_1.LeftChild, None)
        self.assertEqual(root_2_1.RightChild, None)
        self.assertEqual(root_2_1.Level, 2)

        self.assertEqual(root_2_2.NodeKey, 7)
        self.assertEqual(root_2_2.Parent, root_2)
        self.assertEqual(root_2_2.LeftChild, None)
        self.assertEqual(root_2_2.RightChild, None)
        self.assertEqual(root_2_2.Level, 2)

    def test_height_tree(self):
        self.bbst.GenerateTree([2])
        self.assertEqual(self.bbst.tree_height(self.bbst.Root), 0)

        self.bbst.GenerateTree([2, 5, 6])
        self.assertEqual(self.bbst.tree_height(self.bbst.Root), 1)

        self.bbst.GenerateTree([7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(self.bbst.tree_height(self.bbst.Root), 2)

        self.bbst.GenerateTree([7, 6, 5, 4])
        self.assertEqual(self.bbst.tree_height(self.bbst.Root), 2)

    def test_height_tree_custom(self):
        root = main.BSTNode(5, None)

        root_1 = main.BSTNode(4, root)
        root_2 = main.BSTNode(8, root)
        root.LeftChild = root_1
        root.RightChild = root_2

        root_1_1 = main.BSTNode(3, root_1)
        root_1.LeftChild = root_1_1

        root_2_1 = main.BSTNode(6, root_2)
        root_2.LeftChild = root_2_1

        root_1_1_1 = main.BSTNode(2, root_1_1)
        root_1_1.LeftChild = root_1_1_1

        root_1_1_1_1 = main.BSTNode(1, root_1_1_1)
        root_1_1_1.LeftChild = root_1_1_1_1

        self.bbst.Root = root
        self.assertEqual(self.bbst.tree_height(self.bbst.Root), 4)

    def test_is_balanced_true(self):
        self.bbst.GenerateTree([2])
        self.assertEqual(self.bbst.IsBalanced(self.bbst.Root), True)

        self.bbst.GenerateTree([2, 5, 6])
        self.assertEqual(self.bbst.IsBalanced(self.bbst.Root), True)

        self.bbst.GenerateTree([7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(self.bbst.IsBalanced(self.bbst.Root), True)

        self.bbst.GenerateTree([7, 6, 5, 4])
        self.assertEqual(self.bbst.IsBalanced(self.bbst.Root), True)

    def test_is_balanced_false_case_1(self):
        root = main.BSTNode(5, None)

        root_1 = main.BSTNode(3, root)
        root_2 = main.BSTNode(10, root)
        root.LeftChild = root_1
        root.RightChild = root_2

        root_1_1 = main.BSTNode(2, root_1)
        root_1.LeftChild = root_1_1

        root_2_1 = main.BSTNode(9, root_2)
        root_2.LeftChild = root_2_1

        root_1_1_1 = main.BSTNode(1, root_1_1)
        root_1_1.LeftChild = root_1_1_1

        self.bbst.Root = root
        self.assertEqual(self.bbst.IsBalanced(self.bbst.Root), False)

if __name__ == '__main__':
    unittest.main()
