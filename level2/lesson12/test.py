import random
import unittest


import main


class NativeCache(unittest.TestCase):

    def setUp(self):
        self.native_dict = main.NativeCache(5)
        self.native_dict.put('one', 1)
        self.native_dict.put('two', 2)
        self.native_dict.put(3, 3)
        self.native_dict.put('four', 4)
        self.native_dict.put('five', 5)

    def test_put_in_free_slots(self):
        self.assertEqual(self.native_dict.slots, ['five', 'two', 'one', 3, 'four'])
        self.assertEqual(self.native_dict.values, [5, 2, 1, 3, 4])

    def test_hits_slots(self):
        self.assertEqual(self.native_dict.hits, [0, 0, 0, 0, 0])

        self.native_dict.get('no_key')
        self.assertEqual(self.native_dict.hits, [0, 0, 0, 0, 0])

        self.native_dict.get('one')
        self.native_dict.get('one')
        self.native_dict.is_key('one')
        self.assertEqual(self.native_dict.hits, [0, 0, 3, 0, 0])

        self.native_dict.put('one', 1)
        self.assertEqual(self.native_dict.hits, [0, 0, 0, 0, 0])

        self.native_dict.get('four')
        self.native_dict.get('five')
        self.assertEqual(self.native_dict.hits, [1, 0, 0, 0, 1])

    def test_rewrite_slots(self):
        self.native_dict.get('one')
        self.native_dict.get('two')
        self.native_dict.get('four')
        self.native_dict.get('five')
        self.native_dict.put('three', 33333)

        self.assertEqual(self.native_dict.slots, ['five', 'two', 'one', 'three', 'four'])
        self.assertEqual(self.native_dict.values, [5, 2, 1, 33333, 4])
        self.assertEqual(self.native_dict.hits, [1, 1, 1, 0, 1])


if __name__ == '__main__':
    unittest.main()
