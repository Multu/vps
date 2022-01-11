class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        if None in self.vertex:
            free_index = self.vertex.index(None)
            self.vertex[free_index] = Vertex(v)

    def RemoveVertex(self, v):
        if self.is_correct_vertex_index(v):
            self.vertex[v] = None
            for i in range(self.max_vertex):
                self.m_adjacency[v][i] = 0
            for i in range(self.max_vertex):
                self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        if self.is_correct_vertex_index(v1) and self.is_correct_vertex_index(v2):
            return self.m_adjacency[v1][v2]
        return False

    def AddEdge(self, v1, v2):
        if self.is_correct_vertex_index(v1) and self.is_correct_vertex_index(v2):
            self.m_adjacency[v1][v2] = 1

    def RemoveEdge(self, v1, v2):
        if self.is_correct_vertex_index(v1) and self.is_correct_vertex_index(v2):
            self.m_adjacency[v1][v2] = 0

    def is_correct_vertex_index(self, v):
        return 0 <= v < self.max_vertex
