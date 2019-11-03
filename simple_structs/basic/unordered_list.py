class Node():
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while found is False:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        found = False
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.get_next()
            count += 1

        return count

    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current is None:
            previous = current
            current = current.get_next()

        previous.set_next(temp)

    def insert(self, position, item):
        pass

    def index(self, item):
        count = 0
        found = False
        current = self.head
        while current is not None and found is False:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                count += 1

        return count

    def pop(self, item):
        self.remove(item)
        return item


if __name__ == "__main__":
    lst = UnorderedList()
    for i in range(0, 11):
        lst.add(i)

    print(lst.size())
    print(lst.search(2))
    lst.remove(5)
    print(lst.size())
    print(lst.index(4))
    print(lst.pop(1))
    print(lst.size())
    lst.append(77)
    print(lst.index(77))
