import random
import unittest


import main


class HashTable(unittest.TestCase):

    def test_hash_fun(self):
        hash_table = main.HashTable(17, 3)

        self.assertEqual(hash_table.hash_fun('123'), 14)
        self.assertEqual(hash_table.hash_fun(''), 0)
        self.assertEqual(hash_table.hash_fun('test'), 6)
        self.assertEqual(hash_table.hash_fun('super hash'), 8)

    def test_seek_slot_empty_table(self):
        hash_table = main.HashTable(17, 3)

        self.assertEqual(hash_table.seek_slot('123'), 14)
        self.assertEqual(hash_table.seek_slot(''), 0)
        self.assertEqual(hash_table.seek_slot('test'), 6)
        self.assertEqual(hash_table.seek_slot('super hash'), 8)

    def test_seek_slot_half_full(self):
        hash_table = main.HashTable(17, 3)

        # Pre-fill first 10 slots.
        pre_fill_values = ['3', '4', '5', '6', '7', '8', '9', ':', ';', '<']
        for i in range(len(pre_fill_values)):
            hash_table.put(pre_fill_values[i])

        # Seek key, than already exists in hash table.
        self.assertEqual(hash_table.seek_slot('3'), None)

        # Seek unique keys.
        self.assertEqual(hash_table.seek_slot('123'), 14)
        self.assertEqual(hash_table.seek_slot(''), 12)
        self.assertEqual(hash_table.seek_slot('test'), 12)
        self.assertEqual(hash_table.seek_slot('super hash'), 11)

    def test_seek_slot_full(self):
        hash_table = main.HashTable(17, 3)

        # Pre-fill all slots.
        pre_fill_values = [
            '3', '4', '5', '6', '7', '8', '9', ':', ';',
            '<', '=', '>', '?', '@', 'A', 'B', 'C',
        ]
        for i in range(len(pre_fill_values)):
            hash_table.put(pre_fill_values[i])

        self.assertEqual(hash_table.seek_slot('123'), None)
        self.assertEqual(hash_table.seek_slot(''), None)
        self.assertEqual(hash_table.seek_slot('test'), None)
        self.assertEqual(hash_table.seek_slot('super hash'), None)

    def test_put(self):
        hash_table = main.HashTable(17, 3)

        self.assertEqual(hash_table.put('A'), 14)
        self.assertEqual(hash_table.put('B'), 15)
        self.assertEqual(hash_table.put('R'), 0)
        self.assertEqual(hash_table.put('I'), 5)
        self.assertEqual(hash_table.put('F'), 2)
        self.assertEqual(hash_table.put('a'), 12)
        self.assertEqual(hash_table.put('3'), 3)
        self.assertEqual(hash_table.put('7'), 4)
        self.assertEqual(hash_table.put('h'), 8)
        self.assertEqual(hash_table.put('t'), 6)
        self.assertEqual(hash_table.put('w'), 9)
        self.assertEqual(hash_table.put('5'), 11)
        self.assertEqual(hash_table.put('3'), None)
        self.assertEqual(hash_table.put('b'), 13)
        self.assertEqual(hash_table.put('k'), 1)
        self.assertEqual(hash_table.put('Z'), 7)
        self.assertEqual(hash_table.put('V'), 10)
        self.assertEqual(hash_table.put('W'), 16)
        self.assertEqual(hash_table.put('U'), None)

    def test_find(self):
        hash_table = main.HashTable(17, 3)

        # Pre-fill slots.
        pre_fill_values = [
            'A', 'B', 'R', 'I', 'F', 'a', '3', '7', 'h', 't', 'w', '5'
        ]
        for i in range(len(pre_fill_values)):
            hash_table.put(pre_fill_values[i])

        self.assertEqual(hash_table.find('4'), None)
        self.assertEqual(hash_table.find('h'), 8)
        self.assertEqual(hash_table.find('3'), 3)
        self.assertEqual(hash_table.find('W'), None)
        self.assertEqual(hash_table.find('F'), 2)


if __name__ == '__main__':
    unittest.main()
