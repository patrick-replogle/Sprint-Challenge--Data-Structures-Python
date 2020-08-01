class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.oldest_index = 0
        elif len(self.storage) == self.capacity:
            self.storage[self.oldest_index] = item
            self.oldest_index += 1
            if self.oldest_index == self.capacity:
                self.oldest_index = 0

    def get(self):
        return self.storage


r = RingBuffer(3)
r.append('a')
r.append('b')
r.append('c')
r.append('d')
r.append('e')
r.append('f')
print(r.get())
