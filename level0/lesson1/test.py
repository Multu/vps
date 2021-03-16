import unittest

import main


class SquirrelTest(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(main.factorial(0), 1)
        self.assertEqual(main.factorial(1), 1)
        self.assertEqual(main.factorial(2), 2)
        self.assertEqual(main.factorial(10), 3628800)
        self.assertEqual(main.factorial(50), 30414093201713378043612608166064768844377641568960512000000000000)

    def test_squirrel_result_type(self):
        self.assertIsInstance(main.squirrel(0), int)
        self.assertIsInstance(main.squirrel(1), int)
        self.assertIsInstance(main.squirrel(2), int)
        self.assertIsInstance(main.squirrel(10), int)
        self.assertIsInstance(main.squirrel(50), int)

    def test_squirrel_value(self):
        self.assertEqual(main.squirrel(0), 1)
        self.assertEqual(main.squirrel(1), 1)
        self.assertEqual(main.squirrel(2), 2)
        self.assertEqual(main.squirrel(10), 3)
        self.assertEqual(main.squirrel(50), 3)


if __name__ == '__main__':
    unittest.main()
