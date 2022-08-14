class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0
        self.front = 0

    def size(self):
        return self.length

    def iter(self):
        for item in self.queue:
            print(item)

    def add(self, item):
        self.queue.append(item)
        self.length += 1

    def get(self):
        self.length = self.length - 1
        dequeue = self.queue[self.front]
        self.queue = self.queue[1:]
        return dequeue

    def get_first(self):
        return self.queue[self.front]

queue = Queue()
queue.add(3)
queue.add(5)
queue.add(8)

print('1st iter')
queue.iter()
queue.get()
print("size" + str(queue.size()))

print('2nd iter')
queue.iter()
queue.size()
print("size" + str(queue.size()))