import unittest
import random

import main


class SimpleGraph(unittest.TestCase):

    def test_add_vertex(self):
        graph = main.SimpleGraph(2)

        graph.AddVertex(5)
        self.assertEqual(graph.vertex[0].Value, 5)
        self.assertEqual(graph.m_adjacency[0].count(0), 2)

        graph.AddVertex(3)
        self.assertEqual(graph.vertex[1].Value, 3)
        self.assertEqual(graph.m_adjacency[1].count(0), 2)

        graph.AddVertex(7)
        self.assertEqual(graph.vertex[0].Value, 5)
        self.assertEqual(graph.m_adjacency[0].count(0), 2)
        self.assertEqual(graph.vertex[1].Value, 3)
        self.assertEqual(graph.m_adjacency[1].count(0), 2)

    def test_remove_vertex(self):
        graph = main.SimpleGraph(5)

        graph.vertex[1] = main.Vertex(1)
        graph.vertex[2] = main.Vertex(2)
        graph.vertex[4] = main.Vertex(4)
        graph.m_adjacency[1][2] = 1
        graph.m_adjacency[1][4] = 1
        graph.m_adjacency[2][1] = 1
        graph.m_adjacency[4][1] = 1

        graph.RemoveVertex(1)
        self.assertEqual(graph.vertex[1], None)
        self.assertEqual(graph.m_adjacency[1][2], 0)
        self.assertEqual(graph.m_adjacency[1][4], 0)
        self.assertEqual(graph.m_adjacency[2][1], 0)
        self.assertEqual(graph.m_adjacency[4][1], 0)

        graph.RemoveVertex(8)

    def test_is_edge(self):
        graph = main.SimpleGraph(5)

        graph.vertex[1] = main.Vertex(1)
        graph.vertex[2] = main.Vertex(2)
        graph.vertex[4] = main.Vertex(4)
        graph.m_adjacency[1][2] = 1
        graph.m_adjacency[1][4] = 1

        self.assertEqual(graph.IsEdge(1, 2), True)
        self.assertEqual(graph.IsEdge(1, 4), True)
        self.assertEqual(graph.IsEdge(2, 1), False)
        self.assertEqual(graph.IsEdge(4, 1), False)
        self.assertEqual(graph.IsEdge(1, 10), False)

    def test_add_edge(self):
        graph = main.SimpleGraph(5)

        graph.vertex[1] = main.Vertex(1)
        graph.vertex[2] = main.Vertex(2)
        graph.vertex[4] = main.Vertex(4)

        self.assertEqual(graph.m_adjacency[1][2], 0)
        graph.AddEdge(1, 2)
        self.assertEqual(graph.m_adjacency[1][2], 1)

    def test_remove_edge(self):
        graph = main.SimpleGraph(5)

        graph.vertex[1] = main.Vertex(1)
        graph.vertex[2] = main.Vertex(2)
        graph.vertex[4] = main.Vertex(4)
        graph.m_adjacency[1][2] = 1
        graph.m_adjacency[1][4] = 1

        graph.RemoveEdge(1, 2)
        self.assertEqual(graph.m_adjacency[1][2], 0)

if __name__ == '__main__':
    unittest.main()
