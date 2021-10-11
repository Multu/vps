class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.prev = None
            newNode.next = self.head
        self.head = newNode

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []

        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next

        return found_nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None:
                    self.head = node.next
                else:
                    node.prev.next = node.next

                if node.next is None:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev

                if all is False:
                    return

            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)

        node = self.head
        while node is not None:
            if node is afterNode:
                newNode.prev = node
                newNode.next = node.next
                if newNode.next is None:
                    self.tail = newNode
                else:
                    newNode.next.prev = newNode
                node.next = newNode
                return

            node = node.next
