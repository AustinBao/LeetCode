class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def add(self, data):
        newnode = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newnode

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def erase(self,index):
        if index >= self.length():
            return False
        curindex = 0
        curnode = self.head
        while True:
            previousnode = curnode
            curnode = curnode.next
            if curindex == index:
                previousnode.next = curnode.next
                return
            curindex += 1




mine = LinkedList()
mine.add(1)
mine.add(4)
mine.add(2)
mine.add(3)
mine.display()
mine.erase(0)
mine.display()