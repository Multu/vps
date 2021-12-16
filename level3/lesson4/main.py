class aBST:

    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        node_index = 0

        while node_index < len(self.Tree):
            node_key = self.Tree[node_index]
            if node_key is None:
                return -1 * node_index
            if key == node_key:
                return node_index

            if key < node_key:
                node_index = node_index * 2 + 1
            else:
                node_index = node_index * 2 + 2

        return None

    def AddKey(self, key):
        node_index = self.FindKeyIndex(key)

        if node_index is None:
            return -1

        if node_index <= 0:
            node_index = -1 * node_index
            self.Tree[node_index] = key

        return node_index
