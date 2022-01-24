class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.dfs_stack = []

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

    def reset_dfs(self):
        self.dfs_stack = []

        for i in range(self.max_vertex):
            if self.vertex[i] is not None:
                self.vertex[i].Hit = False

    def DepthFirstSearch(self, VFrom, VTo):
        self.reset_dfs()

        vertex = self.vertex[VFrom]
        vertex.Hit = True
        self.dfs_stack.append(VFrom)

        while len(self.dfs_stack):
            VFrom = self.dfs_stack[-1]

            if self.IsEdge(VFrom, VTo):
                self.dfs_stack.append(VTo)
                break

            VNext = -1
            for i in range(self.max_vertex):
                if self.m_adjacency[VFrom][i] == 1:
                    vertex = self.vertex[i]
                    if vertex.Hit is False:
                        VNext = i
                        vertex.Hit = True
                        self.dfs_stack.append(i)
                        break

            if VNext < 0:
                self.dfs_stack.pop(VTo)

        dfs_vertex = []
        for vertex_ind in self.dfs_stack:
            dfs_vertex.append(self.vertex[vertex_ind])
        return dfs_vertex
