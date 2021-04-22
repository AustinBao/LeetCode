word = "bbettez"


def Unique(newstring):
    dictionary = {}
    for i in range(len(newstring)):
        if newstring[i] not in dictionary:
            dictionary[newstring[i]] = 1
        else:
            dictionary[newstring[i]] = -1

    for i in range(len(newstring)):
        if dictionary[newstring[i]] == 1:
            return i
    return -1


test = Unique(word)
print(test)
