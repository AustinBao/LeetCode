def ArrangeBooks(shelf):
    shelflist = []
    for i in shelf:
        shelflist.append(i)

    counter = 0
    for index, letters in enumerate(shelflist):
        if letters == "M" or letters == "S":
            sublist = shelflist[index:]

    return counter


print(ArrangeBooks("LMMMSLL"))

print(ArrangeBooks("LMLLMSMS"))

