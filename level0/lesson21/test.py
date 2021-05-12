import unittest
import random
import os

import main


class BiggerGreaterTest(unittest.TestCase):

    def test_case_regression(self):
        self.assertEqual(main.BiggerGreater('ая'), 'яа')
        self.assertEqual(main.BiggerGreater('нклм'), 'нкмл')
        self.assertEqual(main.BiggerGreater('вибк'), 'викб')
        self.assertEqual(main.BiggerGreater('вкиб'), 'ибвк')
        self.assertEqual(main.BiggerGreater('вкиб'), 'ибвк')

        self.assertEqual(main.BiggerGreater('fff'), '')
        self.assertEqual(main.BiggerGreater('edcba'), '')
        self.assertEqual(main.BiggerGreater('edccc'), '')
        self.assertEqual(main.BiggerGreater('a'), '')

        self.assertEqual(main.BiggerGreater('abc'), 'acb')
        self.assertEqual(main.BiggerGreater('aab'), 'aba')
        self.assertEqual(main.BiggerGreater('abcdef'), 'abcdfe')
        self.assertEqual(main.BiggerGreater('ebkkc'), 'ecbkk')
        self.assertEqual(main.BiggerGreater('efkkc'), 'ekcfk')
        self.assertEqual(main.BiggerGreater('zvrlyvyqixbicinmymjl'), 'zvrlyvyqixbicinmymlj')
        self.assertEqual(main.BiggerGreater('ngoysqgaghkvdikoqwzk'), 'ngoysqgaghkvdkikoqwz')

if __name__ == '__main__':
    unittest.main()
