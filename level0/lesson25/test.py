import unittest
import random
import os

import main


class TransformTransformTest(unittest.TestCase):

    def test_case_regression(self):
        self.assertEqual(main.TransformTransform([1], 1), False)
        self.assertEqual(main.TransformTransform([2], 1), True)
        self.assertEqual(main.TransformTransform([2, 5], 2), False)
        self.assertEqual(main.TransformTransform([2, 2], 2), True)
        self.assertEqual(main.TransformTransform([3, 2, 1], 3), True)

if __name__ == '__main__':
    unittest.main()
