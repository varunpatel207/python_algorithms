class Stack:
    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def is_empty(self):
        return True if not self.stack else False

    def __repr__(self):
        return self.stack

    def __str__(self):
        return str(self.stack)

stack = Stack(limit=10)
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(1)
print(stack)
stack.pop()
print(stack)
