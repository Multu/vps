import unittest
import random

import main


class SynchronizingTablesTest(unittest.TestCase):

    def test_example(self):
        ids = [50, 1, 1024]
        salary = [20000, 100000, 90000]
        output = [90000, 20000, 100000]

        self.assertEqual(main.SynchronizingTables(len(ids), ids, salary), output)

    def test_one_element(self):
        ids = [300]
        salary = [1000]
        output = [1000]

        self.assertEqual(main.SynchronizingTables(len(ids), ids, salary), output)

    def test_same_salary(self):
        ids = [1, 2, 3, 4, 5, 6, 7]
        salary = [5000, 5000, 5000, 5000, 5000, 5000, 5000]
        output = [5000, 5000, 5000, 5000, 5000, 5000, 5000]
        self.assertEqual(main.SynchronizingTables(len(ids), ids, salary), output)

    def test_contains_same_salary(self):
        ids = [50, 13, 5, 8, 15, 1, 33]
        salary = [5000, 3500, 1000, 2000, 1000, 5000, 1000]
        output = [5000, 2000, 1000, 1000, 3500, 1000, 5000]
        self.assertEqual(main.SynchronizingTables(len(ids), ids, salary), output)

    def test_random(self):
        ids = list(range(1, 51))
        salary = list(range(1000, 51000, 1000))

        for i in range(1000):
            random.shuffle(ids)
            random.shuffle(salary)

            output = []
            for j in range(len(ids)):
                output.append(ids[j] * 1000)

            self.assertEqual(main.SynchronizingTables(len(ids), ids, salary), output)

if __name__ == '__main__':
    unittest.main()
