class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        new_node = Node(value)

        if self.len() == 0:
            self.head = new_node
            self.tail = new_node
            return

        node = self.head
        if self.__ascending is True:
            while node is not None and self.compare(value, node.value) > 0:
                node = node.next
        else:
            while node is not None and self.compare(value, node.value) < 0:
                node = node.next

        if node is None:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        elif node.prev is None:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node

    def find(self, val):
        node = self.head
        while node is not None:
            comparison = self.compare(val, node.value)
            if comparison == 0:
                return node
            elif (
                    self.__ascending is True and comparison < 0
                    or
                    self.__ascending is False and comparison > 0
            ):
                return None

            node = node.next

        return None

    def delete(self, val):
        node = self.find(val)
        if node is not None:
            if node.prev is None:
                self.head = node.next
            else:
                node.prev.next = node.next

            if node.next is None:
                self.tail = node.prev
            else:
                node.next.prev = node.prev

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()

        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0
