class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

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

        if node is None:
            return

        # Remove from head.
        while node.value == val:
            self.head = node.next
            if self.head is None:
                self.tail = None
                return

            if all is True:
                node = self.head
            else:
                return

        # Remove from rest of linked list.
        while node.next is not None:
            next_node = node.next
            if next_node.value == val:
                node.next = next_node.next
                if node.next is None:
                    self.tail = node
                    return

                if all is False:
                    return
            else:
                node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        elements_count = 0

        node = self.head
        while node is not None:
            elements_count += 1
            node = node.next

        return elements_count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if newNode.next is None:
                self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node is afterNode:
                    newNode.next = node.next
                    node.next = newNode
                    if newNode.next is None:
                        self.tail = newNode
                    break
                node = node.next
