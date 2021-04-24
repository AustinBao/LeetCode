exampleList = [1, 3, 1, 4, 4]

newlist = []

def single(lista):
    # See if you can solve this issue using no nested for loops and a dictionary
    for n in lista:
        if n not in newlist:
            newlist.append(n)
        else:
            newlist.remove(n)
    return newlist

test1 = single(exampleList)
print(test1)