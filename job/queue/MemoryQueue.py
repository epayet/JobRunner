class MemoryQueue:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def get_nb_data(self):
        return len(self.list)

    def clear_queue(self):
        del self.list[:]

    def pop(self):
        return self.list.pop()
