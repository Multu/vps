class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        sorted_values = sorted(a)
        self.Root = self.tree_builder(None, sorted_values)

    def tree_builder(self, root, sorted_values_slice):
        if len(sorted_values_slice):
            node_index = len(sorted_values_slice) // 2
            node_key = sorted_values_slice[node_index]

            node = BSTNode(node_key, root)
            if root is not None:
                node.Level = root.Level + 1
            node.LeftChild = self.tree_builder(node, sorted_values_slice[:node_index])
            node.RightChild = self.tree_builder(node, sorted_values_slice[node_index + 1:])

            return node
        else:
            return None

    def tree_height(self, root_node):
        if root_node is None:
            return -1

        left_height = self.tree_height(root_node.LeftChild)
        right_height = self.tree_height(root_node.RightChild)
        return max(left_height, right_height) + 1

    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        return (self.IsBalanced(root_node.LeftChild) and
                self.IsBalanced(root_node.RightChild) and
                abs(self.tree_height(root_node.LeftChild) - self.tree_height(root_node.RightChild)) <= 1)
