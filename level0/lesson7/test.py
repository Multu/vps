import unittest
import random

import main


class WordSearchTest(unittest.TestCase):

    def test_examples(self):
        examples = [
            [12, 'строка разбивается на набор строк через выравнивание по заданной ширине.', 'строк', [0, 0, 0, 1, 0, 0, 0]],
            [12, 'Современное программное обеспечение и онлайн-сервисы имеют достаточную степень защиты, которая обеспечивает неприкосновенность персональных данных.', 'сы', [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [1, 'оториноларинголог', 'о', [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]],
            [4, 'оториноларинголог', 'г', [0, 0, 0, 0, 1]],
            [4, 'оториноларинголог', 'ото', [0, 0, 0, 0, 0]],
            [10, '', 'о', []],
            [10, 'привет', 'о', [0]],
            [10, 'привет как дела', '', [0, 0]],
            [0, 'привет как дела', '', []],
        ]


        for i in range(len(examples)):
            dataset = examples[i]
            self.assertEqual(main.WordSearch(dataset[0], dataset[1], dataset[2]), dataset[3])

if __name__ == '__main__':
    unittest.main()