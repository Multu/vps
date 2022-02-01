import unittest
import random

import main


class SimpleGraph(unittest.TestCase):

    def get_nodes_values(self, nodes):
        nodes_values = []
        for node in nodes:
            nodes_values.append(node.Value)
        return nodes_values

    def test_weak_vertices_case_1(self):
        graph = main.SimpleGraph(9)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddVertex(4)
        graph.AddVertex(5)
        graph.AddVertex(6)
        graph.AddVertex(7)
        graph.AddVertex(8)
        graph.AddVertex(9)

        graph.AddEdge(0, 1)
        graph.AddEdge(1, 3)
        graph.AddEdge(3, 2)
        graph.AddEdge(2, 0)
        graph.AddEdge(1, 2)
        graph.AddEdge(0, 7)
        graph.AddEdge(7, 4)
        graph.AddEdge(2, 4)
        graph.AddEdge(4, 6)
        graph.AddEdge(6, 5)
        graph.AddEdge(6, 5)
        graph.AddEdge(4, 5)
        graph.AddEdge(5, 8)

        nodes = graph.WeakVertices()
        nodes_values = sorted(self.get_nodes_values(nodes))
        self.assertEqual(nodes_values, [8, 9])

    def test_weak_vertices_case_2(self):
        graph = main.SimpleGraph(9)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddVertex(4)
        graph.AddVertex(5)
        graph.AddVertex(6)
        graph.AddVertex(7)
        graph.AddVertex(8)
        graph.AddVertex(9)

        graph.AddEdge(0, 1)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(2, 4)
        graph.AddEdge(2, 5)
        graph.AddEdge(1, 4)
        graph.AddEdge(3, 5)
        graph.AddEdge(4, 7)
        graph.AddEdge(5, 7)
        graph.AddEdge(4, 6)
        graph.AddEdge(5, 8)
        graph.AddEdge(6, 7)
        graph.AddEdge(7, 8)

        nodes = graph.WeakVertices()
        nodes_values = sorted(self.get_nodes_values(nodes))
        self.assertEqual(nodes_values, [1])

if __name__ == '__main__':
    unittest.main()
