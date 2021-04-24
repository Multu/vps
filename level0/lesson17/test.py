import unittest
import random

import main


class LineAnalysisTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            ['*..*..*..*..*..*..*', True],
            ['*..*..*..*..*..*..**', False],
            ['*..*...*..*..*..*..*', False],
            ['*..*..*..*..*..**..*', False],
            ['*', True],
            ['***', True],
            ['*.......*.......*', True],
            ['**', True],
            ['*.*', True],
            ['.', False],
            ['...', False],
            ['*.*.', False],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.LineAnalysis(dataset[0]), dataset[1])

if __name__ == '__main__':
    unittest.main()
