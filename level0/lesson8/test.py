import unittest
import random

import main


class WordSearchTest(unittest.TestCase):

    def test_examples(self):
        in_data = [5, -25, 10, -35, -45]
        out_data = -45

        for i in range(100):
            random.shuffle(in_data)
            self.assertEqual(main.SumOfThe(len(in_data), in_data), out_data)


        in_data = [100 , -50, 10, -25, 90, -35, 90]
        out_data = 90

        for i in range(100):
            random.shuffle(in_data)
            self.assertEqual(main.SumOfThe(len(in_data), in_data), out_data)

    def test_random(self):
        for i in range(1000):
            n = random.randint(1, 20)

            in_data = random.sample(range(-100, 100), n)
            out_data = sum(in_data)
            in_data.append(out_data)

            for j in range(100):
                random.shuffle(in_data)
                self.assertEqual(main.SumOfThe(len(in_data), in_data), out_data)


if __name__ == '__main__':
    unittest.main()
