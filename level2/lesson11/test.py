import random
import unittest
import time


import main


class BloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloom_filter = main.BloomFilter(32)

    def test_hash1(self):
        self.assertEqual(self.bloom_filter.hash1('0123456789'), 13)
        self.assertEqual(self.bloom_filter.hash1('xyz'), 27)
        self.assertEqual(self.bloom_filter.hash1(''), 0)

    def test_hash2(self):
        self.assertEqual(self.bloom_filter.hash2('0123456789'), 5)
        self.assertEqual(self.bloom_filter.hash2('xyz'), 25)
        self.assertEqual(self.bloom_filter.hash2(''), 0)

    def test_add(self):
        self.bloom_filter.add('0123456789')
        self.assertEqual(self.bloom_filter.bitmap, 8224)

        self.bloom_filter.add('1234567890')
        self.assertEqual(self.bloom_filter.bitmap, 671096864)

        self.bloom_filter.add('2345678901')
        self.assertEqual(self.bloom_filter.bitmap, 671096864)

        self.bloom_filter.add('3456789012')
        self.assertEqual(self.bloom_filter.bitmap, 671096864)

        self.bloom_filter.add('4567890123')
        self.assertEqual(self.bloom_filter.bitmap, 671096864)

    def test_is_value(self):
        self.assertEqual(self.bloom_filter.is_value('0123456789'), False)
        self.assertEqual(self.bloom_filter.is_value('xyz'), False)

        self.bloom_filter.bitmap = 8224
        self.assertEqual(self.bloom_filter.is_value('0123456789'), True)
        self.assertEqual(self.bloom_filter.is_value('2345678901'), True)
        self.assertEqual(self.bloom_filter.is_value('4567890123'), True)
        self.assertEqual(self.bloom_filter.is_value('1234567890'), False)

if __name__ == '__main__':
    unittest.main()


