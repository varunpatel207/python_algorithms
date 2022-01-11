class Stack:
    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def __repr__(self):
        return self.stack

    def __str__(self):
        return str(self.stack)

stack = Stack(limit=10)
stack.push(1)
stack.push(2)

print(stack)
