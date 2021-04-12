exampleList = [1, 3, 1, 4, 4]

newlist = []

def single(lista):
    for n in lista:
        if n not in newlist:
            newlist.append(n)
        else:
            newlist.remove(n)
    return newlist

test1 = single(exampleList)
print(test1)