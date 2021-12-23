import unittest
import random

import main


class BBSTArray(unittest.TestCase):

    def test_generate_BBST_height_0(self):
        all_nodes = list(range(1, 2))
        self.assertEqual(main.GenerateBBSTArray(all_nodes), [1])

    def test_generate_BBST_height_1(self):
        all_nodes = list(range(1, 4))

        for i in range(5):
            random.shuffle(all_nodes)
            self.assertEqual(main.GenerateBBSTArray(all_nodes), [2, 1, 3])

    def test_generate_BBST_height_2(self):
        all_nodes = list(range(1, 8))

        for i in range(50):
            random.shuffle(all_nodes)
            self.assertEqual(main.GenerateBBSTArray(all_nodes), [4, 2, 6, 1, 3, 5, 7])


if __name__ == '__main__':
    unittest.main()
