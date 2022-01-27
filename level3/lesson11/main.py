class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode

        if ParentNode is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        if self.Root is None:
            return []

        all_nodes = []
        parent_nodes = [self.Root]
        while len(parent_nodes):
            parent_node = parent_nodes.pop(0)
            for child_node in parent_node.Children:
                parent_nodes.append(child_node)
            all_nodes.append(parent_node)
        return all_nodes

    def FindNodesByValue(self, val):
        found_nodes = []
        for node in self.GetAllNodes():
            if node.NodeValue == val:
                found_nodes.append(node)
        return found_nodes

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        leaf_count = 0
        for node in self.GetAllNodes():
            if len(node.Children) == 0:
                leaf_count += 1
        return leaf_count


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop()

    def size(self):
        return len(self.queue)


class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


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

    def reset_vertex_hits(self):
        for i in range(self.max_vertex):
            if self.vertex[i] is not None:
                self.vertex[i].Hit = False

    def BreadthFirstSearch(self, VFrom, VTo):
        self.reset_vertex_hits()
        bfs_queue = Queue()
        path_tree = SimpleTree(None)

        vertex = self.vertex[VFrom]
        vertex.Hit = True
        parent_path_node = SimpleTreeNode(VFrom, None)
        path_tree.AddChild(None, parent_path_node)

        while vertex is not None:

            if self.IsEdge(VFrom, VTo):
                path_node = SimpleTreeNode(VTo, parent_path_node)
                path_tree.AddChild(parent_path_node, path_node)
                break

            for i in range(self.max_vertex):
                if self.m_adjacency[VFrom][i] == 1:
                    edged_vertex = self.vertex[i]
                    if edged_vertex.Hit is False:
                        edged_vertex.Hit = True

                        bfs_queue.enqueue(i)

                        path_node = SimpleTreeNode(i, parent_path_node)
                        path_tree.AddChild(parent_path_node, path_node)

            if bfs_queue.size():
                VFrom = bfs_queue.dequeue()
                vertex = self.vertex[VFrom]
                parent_path_node = path_tree.FindNodesByValue(VFrom)[0]
            else:
                vertex = None

        target_node = None
        target_nodes = path_tree.FindNodesByValue(VTo)
        if len(target_nodes):
            target_node = target_nodes[0]

        bfs_vertex = []
        while target_node is not None:
            bfs_vertex.insert(0, self.vertex[target_node.NodeValue])
            target_node = target_node.Parent

        return bfs_vertex
