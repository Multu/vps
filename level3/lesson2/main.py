class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        node = self.Root
        parent = None
        while node is not None and node.NodeKey != key:
            parent = node
            if key < node.NodeKey:
                node = node.LeftChild
            elif key > node.NodeKey:
                node = node.RightChild

        founded_node = BSTFind()
        if node is not None:
            founded_node.Node = node
            founded_node.NodeHasKey = True
        elif parent is not None:
            founded_node.Node = parent
            if key < parent.NodeKey:
                founded_node.ToLeft = True
        return founded_node

    def AddKeyValue(self, key, val):
        founded_node = self.FindNodeByKey(key)

        if founded_node.NodeHasKey is True:
            return False

        new_node = BSTNode(key, val, founded_node.Node)
        if founded_node.Node is not None:
            if founded_node.ToLeft is True:
                founded_node.Node.LeftChild = new_node
            else:
                founded_node.Node.RightChild = new_node
        else:
            self.Root = new_node

        return True

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        founded_node = None
        while node is not None:
            founded_node = node
            if FindMax is True:
                node = node.RightChild
            else:
                node = node.LeftChild
        return founded_node

    def DeleteNodeByKey(self, key):
        bst_find = self.FindNodeByKey(key)
        if bst_find.NodeHasKey is False:
            return False

        node_for_delete = bst_find.Node

        if node_for_delete.LeftChild and node_for_delete.RightChild:
            receiver_node = node_for_delete.RightChild
            while receiver_node.LeftChild is not None:
                receiver_node = receiver_node.LeftChild

            receiver_node_child = receiver_node.RightChild
            if receiver_node_child is not None:
                receiver_node_child.Parent = receiver_node.Parent

            receiver_node_position = self.LeftOrRightChild(receiver_node)
            if receiver_node_position < 0:
                receiver_node.Parent.LeftChild = receiver_node_child
            elif receiver_node_position > 0:
                receiver_node.Parent.RightChild = receiver_node_child

            receiver_node.LeftChild = node_for_delete.LeftChild
            receiver_node.RightChild = node_for_delete.RightChild
            receiver_node.Parent = node_for_delete.Parent

        else:
            receiver_node = None
            if node_for_delete.RightChild is not None:
                receiver_node = node_for_delete.RightChild
            elif node_for_delete.LeftChild is not None:
                receiver_node = node_for_delete.LeftChild

            if receiver_node is not None:
                receiver_node.Parent = node_for_delete.Parent

        node_for_delete_position = self.LeftOrRightChild(node_for_delete)
        if node_for_delete_position < 0:
            node_for_delete.Parent.LeftChild = receiver_node
        elif node_for_delete_position > 0:
            node_for_delete.Parent.RightChild = receiver_node
        else:
            self.Root = receiver_node

        return True

    def LeftOrRightChild(self, node):
        parent = node.Parent

        if parent is None:
            return 0
        elif parent.LeftChild is node:
            return -1
        elif parent.RightChild is node:
            return 1

    def Count(self):
        nodes_count = self.RecursiveCounting(self.Root, 0)
        return nodes_count

    def RecursiveCounting(self, root, current_count):
        if root is not None:
            left_children_count = self.RecursiveCounting(root.LeftChild, current_count)
            right_children_count = self.RecursiveCounting(root.RightChild, current_count)
            current_count = left_children_count + right_children_count + 1
        return current_count
