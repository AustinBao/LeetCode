linkedlist = [4,5,9,1]
number = 9

def deletenode(head, node):
    for i in range(0, len(head)):
        if head[i] == node:
            head.pop(i)
            return head
    return "none"

test1 = deletenode(linkedlist,number)
print(test1)