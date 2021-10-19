class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]


class StackedQueue:

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def enqueue(self, item):
        self.push_stack.push(item)

    def dequeue(self):
        if self.pop_stack.size() == 0:
            while self.push_stack.size():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

    def size(self):
        return self.push_stack.size() + self.pop_stack.size()
