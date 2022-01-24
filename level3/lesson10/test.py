import unittest
import random

import main


class SimpleGraph(unittest.TestCase):

    def setUp(self):
        graph = main.SimpleGraph(9)
        graph.AddVertex(1)
        graph.AddVertex(5)
        graph.AddVertex(3)
        graph.AddVertex(2)
        graph.AddVertex(4)
        graph.AddVertex(6)
        graph.AddVertex(8)
        graph.AddVertex(7)

        graph.AddEdge(0, 3)
        graph.AddEdge(3, 2)
        graph.AddEdge(3, 4)
        graph.AddEdge(3, 1)
        graph.AddEdge(1, 5)
        graph.AddEdge(5, 7)
        graph.AddEdge(7, 6)
        graph.AddEdge(6, 0)

        self.graph = graph

    def test_exists_path_case_1(self):
        dfs_nodes = self.graph.DepthFirstSearch(3, 0)

        dfs_nodes_values = []
        for node in dfs_nodes:
            dfs_nodes_values.append(node.Value)

        self.assertEqual(dfs_nodes_values, [2, 5, 6, 7, 8, 1])

    def test_exists_path_case_2(self):
        dfs_nodes = self.graph.DepthFirstSearch(6, 2)

        dfs_nodes_values = []
        for node in dfs_nodes:
            dfs_nodes_values.append(node.Value)

        self.assertEqual(dfs_nodes_values, [8, 1, 2, 3])

    def test_not_exists_path_case1(self):
        dfs_nodes = self.graph.DepthFirstSearch(4, 0)

        dfs_nodes_values = []
        for node in dfs_nodes:
            dfs_nodes_values.append(node.Value)

        self.assertEqual(dfs_nodes_values, [])

    def test_not_exists_path_case2(self):
        self.graph.RemoveEdge(6, 0)
        dfs_nodes = self.graph.DepthFirstSearch(1, 2)

        dfs_nodes_values = []
        for node in dfs_nodes:
            dfs_nodes_values.append(node.Value)

        self.assertEqual(dfs_nodes_values, [])

if __name__ == '__main__':
    unittest.main()
