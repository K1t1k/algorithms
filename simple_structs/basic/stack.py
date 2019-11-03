class Stack():
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
