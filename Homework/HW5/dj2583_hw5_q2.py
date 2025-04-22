
class MaxStack:
    def __init__(self):
        self.data = []
        self.max_val = []
        self.n = 0
    def __len__(self):
        return self.n
    def push(self, e):
            self.data.append(e)
            self.n += 1
            if not self.max_val or e >= self.max_val[-1]:
                self.max_val.append(e)
    def is_empty(self):
        return self.n == 0
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data[-1]
    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.max_val[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        val = self.data.pop()
        self.n -= 1
        if self.max_val[-1] == val:
            self.max_val.pop()
        return val


maxS = MaxStack()
maxS.is_empty()	# line 1
maxS.top()	# line 2
maxS.max()	# line 3
maxS.pop()	# line 4
maxS.push(4)	# line 5
maxS.push(1)	# line 6
maxS.push(6)	# line 7
maxS.is_empty()	# line 8
maxS.len()	# line 9
maxS.max()	# line 10
maxS.pop()	# line 11
maxS.max()	# line 12
maxS.pop()	# line 13
maxS.top()