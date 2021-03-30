import unittest
import random

import main


class PrintingCostsTest(unittest.TestCase):

    def test_all_table(self):
        str = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        toner_sum = 1757
        self.assertEqual(main.PrintingCosts(str), toner_sum)

    def test_examples(self):
        data = [
            ['', 0],
            ['         ', 0],
            ['      1  3  !', 51],
            ['№', 23],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.PrintingCosts(dataset[0]), dataset[1])

    def test_random(self):
        ascii_list = list(main.ancii_toner)

        for i in range(10000):
            random.shuffle(ascii_list)
            k = random.randint(0, len(ascii_list))

            str_list = []
            toner_sum = 0
            for j in range(k):
                str_list.append(ascii_list[j][0])
                toner_sum += ascii_list[j][1]
            str = ''.join(str_list)

            self.assertEqual(main.PrintingCosts(str), toner_sum)


if __name__ == '__main__':
    unittest.main()
