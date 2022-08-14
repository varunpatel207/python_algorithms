command_list = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
value_list = [[3], [1], [2], [3], [4], [], [], [], [4], []]


class CircularQueue:
    def __init__(self, limit):
        self.queue = [None] * limit
        self.front = 0
        self.rear = 0

    def enQueue(self, item):
        pass

