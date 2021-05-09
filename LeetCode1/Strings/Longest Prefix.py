input = ["bba", "bba", "bba"]


def prefix(ourlist):
    prefix = ""

    if len(ourlist) == 0:
        return ""

    for i in range(0, len(ourlist)):
        for j in range(i + 1, len(ourlist)):
            if len(ourlist[i]) > len(ourlist[j]):
                ourlist[i], ourlist[j] = ourlist[j], ourlist[i]
    smallest = len(ourlist[0])

    i = 0
    while i < smallest:
        firstletter = ourlist[0][i]
        for j in range(1, len(ourlist)):
            if ourlist[j][i] != firstletter:
                return prefix
        prefix = prefix + firstletter
        i += 1

    return prefix


run = prefix(input)
print(run)
