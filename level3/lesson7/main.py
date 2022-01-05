class Heap:

    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        heep_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * heep_size

        for key in a:
            if self.Add(key) is False:
                break

    def GetMax(self):
        if self.is_empty():
            return -1

        max_key = self.HeapArray[0]

        last_node_index = self.get_last_node_index()
        self.HeapArray[0] = self.HeapArray[last_node_index]
        self.HeapArray[last_node_index] = None

        target_index = 0
        while True:
            max_child_index = self.get_index_of_max_child(target_index)
            if max_child_index < 0:
                break

            target_key = self.HeapArray[target_index]
            max_child_key = self.HeapArray[max_child_index]

            if target_key < max_child_key:
                self.HeapArray[target_index], self.HeapArray[max_child_index] = \
                    self.HeapArray[max_child_index], self.HeapArray[target_index]
                target_index = max_child_index
            else:
                break

        return max_key

    def Add(self, key):
        if self.is_full():
            return False

        last_node_index = self.get_last_node_index()
        new_key_index = last_node_index + 1
        self.HeapArray[new_key_index] = key

        while new_key_index > 0:
            parent_index = (new_key_index - 1) // 2
            if key > self.HeapArray[parent_index]:
                self.HeapArray[parent_index], self.HeapArray[new_key_index] = \
                    self.HeapArray[new_key_index], self.HeapArray[parent_index]
                new_key_index = parent_index
            else:
                break

        return True

    def is_empty(self):
        return len(self.HeapArray) == 0 or self.HeapArray[0] is None

    def is_full(self):
        return len(self.HeapArray) == 0 or self.HeapArray[-1] is not None

    def get_last_node_index(self):
        if self.is_empty():
            return -1

        index = 0
        for i in range(1, len(self.HeapArray)):
            if self.HeapArray[i] is not None:
                index = i
            else:
                break
        return index

    def get_index_of_max_child(self, parent_index):
        left_index = 2 * parent_index + 1
        right_index = 2 * parent_index + 2

        if right_index >= len(self.HeapArray):
            return -1

        left_key = self.HeapArray[left_index]
        if left_key is None:
            left_key = -1
        right_key = self.HeapArray[right_index]
        if right_key is None:
            right_key = -1
        max_key = max(left_key, right_key)
        if max_key < 0:
            return -1

        max_key_index = right_index
        if max_key == left_key:
            max_key_index = left_index
        return max_key_index
