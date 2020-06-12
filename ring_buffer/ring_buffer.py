class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.old = 0

    def append(self, item):
        if self.capacity > len(self.data):
            self.data.append(item)
        else:
            self.data[self.old] = item
            if self.old < len(self.data) - 1:
                self.old += 1
            else:
                self.old = 0

    def get(self):
        return self.data
