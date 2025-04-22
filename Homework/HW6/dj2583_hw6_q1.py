from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.n = len(self.data)
    def __len__(self):
        return self.n
    def is_empty(self):
        return self.n == 0
    def enqueue(self, val):
        self.n += 1
        return self.data.add_last(val)

    def dequeue(self):
        self.n -=1
        return self.data.delete_first()
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data.header.next.data
