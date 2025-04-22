
from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.left = ArrayStack()
        self.right = ArrayDeque()
        self.n = len(self.left) + len(self.right)
    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def push(self, item):
        self.right.enqueue_last(item)
        self.n += 1
        if len(self.right) > len(self.left):
            self.left.push(self.right.dequeue_first())

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if self.right.is_empty():
            self.n -= 1
            return self.left.pop()
        self.n -= 1
        return self.right.dequeue_last()

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if not self.right.is_empty():
            return self.right.last()
        return self.left.top()

    def mid_push(self, item):
        self.left.push(item)
        self.n += 1
        if len(self.left) > len(self.right) + 1:
            self.right.enqueue_first(self.left.pop())




