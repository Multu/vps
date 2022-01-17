class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.Level = 0


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

    def SetLevels(self):
        all_nodes = self.GetAllNodes()
        for i in range(len(all_nodes)):
            cur_node = all_nodes[i]
            cur_level = 0

            while cur_node.Parent is not None:
                cur_level += 1
                cur_node = cur_node.Parent

            all_nodes[i].Level = cur_level

    def EvenTrees(self):
        even_trees_nodes = []

        all_nodes = self.GetAllNodes()
        if len(all_nodes) % 2 == 0:
            for node in all_nodes:
                simple_tree = SimpleTree(node)
                if simple_tree.Count() % 2 == 0 and node.Parent is not None:
                    even_trees_nodes.append(node.Parent)
                    even_trees_nodes.append(node)
        return even_trees_nodes
