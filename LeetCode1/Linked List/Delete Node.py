userlist = [4, 5, 1, 9]


class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def get_next(self):
        return self.nextNode

    def set_next(self, inputnode):
        self.nextNode = inputnode

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, value):
        node = LinkedListNode(value, self.head)
        self.head = node

    def delete(self, value):
        current = self.head
        previous = None

        while current is not None:
            if current.get_next() == value:
                if previous is not None:
                    previous.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                return True
            else:
                previous = current
                current = current.get_next()
        return False


me = LinkedList()
me.add(2)
me.add(5)
me.add(3)
me.delete(5)
