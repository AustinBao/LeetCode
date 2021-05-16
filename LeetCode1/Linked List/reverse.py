chi = [1,2,3]


def reverse(ourlist):
    i = 0
    j = -1
    new = []
    while i < len(ourlist):
        new.append(ourlist[j])
        j -= 1
        i += 1
    return new


test = reverse(chi)
print(test)
