import unittest
import random

import main


class SimpleGraph(unittest.TestCase):

    def setUp(self):
        graph = main.SimpleGraph(7)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddVertex(4)
        graph.AddVertex(5)
        graph.AddVertex(6)
        graph.AddVertex(7)

        graph.AddEdge(4, 1)
        graph.AddEdge(1, 5)
        graph.AddEdge(5, 0)
        graph.AddEdge(0, 2)
        graph.AddEdge(2, 6)
        graph.AddEdge(6, 3)

        self.graph = graph

    def get_nodes_values(self, nodes):
        nodes_values = []
        for node in nodes:
            nodes_values.append(node.Value)
        return nodes_values

    def test_not_exists_path_case_1(self):
        nodes = self.graph.BreadthFirstSearch(0, 4)
        nodes_values = self.get_nodes_values(nodes)
        self.assertEqual(nodes_values, [])

    def test_not_exists_path_case_2(self):
        nodes = self.graph.BreadthFirstSearch(3, 2)
        nodes_values = self.get_nodes_values(nodes)
        self.assertEqual(nodes_values, [])

    def test_exists_path_case_1(self):
        nodes = self.graph.BreadthFirstSearch(4, 2)
        nodes_values = self.get_nodes_values(nodes)
        self.assertEqual(nodes_values, [5, 2, 6, 1, 3])

    def test_exists_path_case_2(self):
        nodes = self.graph.BreadthFirstSearch(2, 3)
        nodes_values = self.get_nodes_values(nodes)
        self.assertEqual(nodes_values, [3, 7, 4])

    def test_exists_path_case_3(self):
        nodes = self.graph.BreadthFirstSearch(5, 0)
        nodes_values = self.get_nodes_values(nodes)
        self.assertEqual(nodes_values, [6, 1])

if __name__ == '__main__':
    unittest.main()
