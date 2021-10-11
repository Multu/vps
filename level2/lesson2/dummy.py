class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None
        self.is_custom = True


class DummyNode(Node):

    def __init__(self):
        super().__init__(None)
        self.is_custom = False


class DummyLinkedList2:

    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        item.prev = self.tail.prev
        item.next = self.tail

        self.tail.prev.next = item
        self.tail.prev = item

    def add_in_head(self, newNode):
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def find(self, val):
        node = self.head.next
        while node.is_custom:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []

        node = self.head.next
        while node.is_custom:
            if node.value == val:
                found_nodes.append(node)
            node = node.next

        return found_nodes

    def delete(self, val, all=False):
        node = self.head.next
        while node.is_custom:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev

                if all is False:
                    return

            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        list_len = 0
        node = self.head.next
        while node.is_custom:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)

        node = self.head.next
        while node.is_custom:
            if node is afterNode:
                newNode.prev = node
                newNode.next = node.next
                newNode.next.prev = newNode
                node.next = newNode
                return

            node = node.next
