class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def __len__(self):
        return len(self.queue)

    def size(self):
        return len(self.queue)

    def get(self):
        dequeue = None
        if len(self.queue) > 0:
            dequeue = self.queue[0]
        self.queue = self.queue[1:]
        return dequeue

    def iter(self):
        for item in self.queue:
            print(item)

    def get_first(self):
        return self.queue[0]

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