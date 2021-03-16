import unittest

import main


class SquirrelTest(unittest.TestCase):

    def test_odometer(self):
        self.assertEqual(main.odometer([10, 1]), 10)
        self.assertEqual(main.odometer([10, 1, 20, 0, 0, 15, 4, 5]), 30)
        self.assertEqual(main.odometer([5, 1, 2, 5, 10, 1, 4, 4, 5, 7]), 76)

    def test_odometer_negative(self):
        self.assertEqual(main.odometer([10, 1, -15, 1]), 10)
        self.assertEqual(main.odometer([10, 1, -15, -1]), 10)
        self.assertEqual(main.odometer([-15, -1]), 0)
        self.assertEqual(main.odometer([15, -1]), 0)

    def test_odometer_odd(self):
        self.assertEqual(main.odometer([10, 1, 15]), 10)

if __name__ == '__main__':
    unittest.main()
