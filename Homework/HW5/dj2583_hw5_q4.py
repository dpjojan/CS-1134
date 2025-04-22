from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.input = ArrayStack()
        self.output = ArrayStack()

    def __len__(self):
        return len(self.input) + len(self.output)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, value):
        self.input.push(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.output.is_empty():
            while not self.input.is_empty():
                self.output.push(self.input.pop())
        return self.output.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.output.is_empty():
            while not self.input.is_empty():
                self.output.push(self.input.pop())
        return self.output.top()
