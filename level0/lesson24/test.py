import unittest
import random
import os

import main


class MatrixTurnTest(unittest.TestCase):

    def test_case_regression(self):
        input_matrix = ["123456", "234567", "345678", "456789"]
        output_matrix = ["212345", "343456", "456767", "567898"]
        main.MatrixTurn(input_matrix, 4, 6, 1)
        self.assertEqual(input_matrix, output_matrix)

        input_matrix = ["56", "79"]
        output_matrix = ["97", "65"]
        main.MatrixTurn(input_matrix, 2, 2, 2)
        self.assertEqual(input_matrix, output_matrix)

        input_matrix = ["123", "567"]
        output_matrix = ["765", "321"]
        main.MatrixTurn(input_matrix, 2, 3, 3)
        self.assertEqual(input_matrix, output_matrix)

        input_matrix = ["12", "45", "78"]
        output_matrix = ["74", "81", "52"]
        main.MatrixTurn(input_matrix, 3, 2, 2)
        self.assertEqual(input_matrix, output_matrix)

if __name__ == '__main__':
    unittest.main()
