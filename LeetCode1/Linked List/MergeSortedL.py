def mergenormal(list1, list2):
    new = []
    for i in list1:
        new.append(i)
    for j in list2:
        new.append(j)
    for k in range(0, len(new)):
        for l in range(k + 1, len(new)):
            if new[k] > new[l]:
                new[k], new[l] = new[l], new[k]
    return new


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

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)


list1 = [1, 2, 2, 3, 3]
list2 = [1, 1, 1, 2, 5]
totallist = mergenormal(list1, list2)

callclass = LinkedList()
for t in totallist:
    callclass.add(t)

callclass.display()
