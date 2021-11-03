import random
import unittest


import main


class NativeDictionary(unittest.TestCase):

    def setUp(self):
        self.native_dict = main.NativeDictionary(5)
        self.native_dict.put('one', 1)
        self.native_dict.put('two', 2)
        self.native_dict.put(3, 3)
        self.native_dict.put('four', 4)
        self.native_dict.put('five', 5)

    def test_put_in_free_slots(self):
        self.assertEqual(self.native_dict.slots, ['five', 'two', 'one', 3, 'four'])
        self.assertEqual(self.native_dict.values, [5, 2, 1, 3, 4])

    def test_put_in_full_slots(self):
        self.native_dict.put('one', 11)
        self.native_dict.put('two', 22)
        self.native_dict.put(3, 33)
        self.native_dict.put('four', 44)
        self.native_dict.put('five', 55)

        self.assertEqual(self.native_dict.slots, ['five', 'two', 'one', 3, 'four'])
        self.assertEqual(self.native_dict.values, [55, 22, 11, 33, 44])

    def test_is_key(self):
        self.assertEqual(self.native_dict.is_key('one'), True)
        self.assertEqual(self.native_dict.is_key('two'), True)
        self.assertEqual(self.native_dict.is_key(3), True)
        self.assertEqual(self.native_dict.is_key('four'), True)
        self.assertEqual(self.native_dict.is_key('five'), True)

        self.assertEqual(self.native_dict.is_key('1'), False)
        self.assertEqual(self.native_dict.is_key('test'), False)
        self.assertEqual(self.native_dict.is_key(''), False)
        self.assertEqual(self.native_dict.is_key('long key with spaces'), False)

    def test_get(self):
        self.assertEqual(self.native_dict.get('one'), 1)
        self.assertEqual(self.native_dict.get('two'), 2)
        self.assertEqual(self.native_dict.get(3), 3)
        self.assertEqual(self.native_dict.get('four'), 4)
        self.assertEqual(self.native_dict.get('five'), 5)

        self.assertEqual(self.native_dict.get('1'), None)
        self.assertEqual(self.native_dict.get('test'), None)
        self.assertEqual(self.native_dict.get(''), None)
        self.assertEqual(self.native_dict.get('long key with spaces'), None)


if __name__ == '__main__':
    unittest.main()
