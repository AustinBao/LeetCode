exampleList = [0]
newDict = {}


def single(lista):
<<<<<<< HEAD
    newDict = {}

    for i in range(len(lista)):
        if lista[i] not in newDict:
            newDict[lista[i]] = 1
=======
    # See if you can solve this issue using no nested for loops and a dictionary
    for n in lista:
        if n not in newlist:
            newlist.append(n)
>>>>>>> b2082ddd913661efb22a91d4d55b7ffe15d45b9c
        else:
            newDict[lista[i]] = -1

    for j in newDict:
        if newDict.get(j) == 1:
            return j

    return None


test1 = single(exampleList)
print(test1)
