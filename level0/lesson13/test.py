import unittest
import random

import main


class UfoTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            [[1234, 1777], False, [4660, 6007]],
            [[1234, 1777], True, [668, 1023]],
            [[0, 1, 2], True, [0, 1, 2]],
            [[0, 1, 2, 10], False, [0, 1, 2, 16]],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.UFO(len(dataset[0]), dataset[0], dataset[1]), dataset[2])

    def test_random_hex(self):
        for i in range(1000):
            input_hex = []
            output = []
            for i in range(random.randint(1, 10)):
                hex = random.randint(0, 100000000)
                decimal = int(str(hex), 16)

                input_hex.append(hex)
                output.append(decimal)

            self.assertEqual(main.UFO(len(input_hex), input_hex, False), output)

    def test_random_oct(self):
        for i in range(1000):
            input_oct = []
            output = []

            for i in range(random.randint(1, 10)):
                try:
                    oct = random.randint(0, 100000000)
                    decimal = int(str(oct), 8)

                    input_oct.append(oct)
                    output.append(decimal)
                except ValueError:
                    pass

            self.assertEqual(main.UFO(len(input_oct), input_oct, True), output)

if __name__ == '__main__':
    unittest.main()
