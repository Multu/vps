import unittest

import main


class aBST(unittest.TestCase):

    """
        Full tree. Example below:
                         10
                 5              15
            3        7      12       18
          1   4                   16
    """
    def setUp(self):
        a_bst = main.aBST(3)
        a_bst.Tree[0] = 10
        a_bst.Tree[1] = 5
        a_bst.Tree[2] = 15
        a_bst.Tree[3] = 3
        a_bst.Tree[4] = 7
        a_bst.Tree[5] = 12
        a_bst.Tree[6] = 18
        a_bst.Tree[7] = 1
        a_bst.Tree[8] = 4
        a_bst.Tree[9] = None
        a_bst.Tree[10] = None
        a_bst.Tree[11] = None
        a_bst.Tree[12] = None
        a_bst.Tree[13] = 16
        a_bst.Tree[14] = None
        self.a_bst = a_bst

        self.a_bst_empty = main.aBST(3)

    def test_tree_size(self):
        tree = main.aBST(0)
        self.assertEqual(len(tree.Tree), 1)

        tree = main.aBST(1)
        self.assertEqual(len(tree.Tree), 3)

        tree = main.aBST(2)
        self.assertEqual(len(tree.Tree), 7)

        tree = main.aBST(3)
        self.assertEqual(len(tree.Tree), 15)

    def test_find_key_index(self):
        self.assertEqual(self.a_bst.FindKeyIndex(6), -9)
        self.assertEqual(self.a_bst.FindKeyIndex(8), -10)
        self.assertEqual(self.a_bst.FindKeyIndex(2), None)
        self.assertEqual(self.a_bst.FindKeyIndex(15), 2)
        self.assertEqual(self.a_bst.FindKeyIndex(10), 0)
        self.assertEqual(self.a_bst.FindKeyIndex(100), -14)

        self.assertEqual(self.a_bst_empty.FindKeyIndex(6), 0)

    def test_add_key(self):
        self.assertEqual(self.a_bst.AddKey(6), 9)
        self.assertEqual(self.a_bst.AddKey(8), 10)
        self.assertEqual(self.a_bst.AddKey(2), -1)
        self.assertEqual(self.a_bst.AddKey(15), 2)
        self.assertEqual(self.a_bst.AddKey(10), 0)
        self.assertEqual(self.a_bst.AddKey(100), 14)
        self.assertEqual(self.a_bst.AddKey(11), 11)
        self.assertEqual(self.a_bst.AddKey(13), 12)
        self.assertEqual(self.a_bst.AddKey(99), -1)


if __name__ == '__main__':
    unittest.main()
