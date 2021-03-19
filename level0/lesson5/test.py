import unittest
import random

import main


class SynchronizingTablesTest(unittest.TestCase):

    def test_one(self):
        ids = [50, 1, 1024]
        salary = [20000, 100000, 90000]
        output = [90000, 20000, 100000]

        self.assertEqual(main.SynchronizingTables(len(ids), ids, salary), output)

if __name__ == '__main__':
    unittest.main()
