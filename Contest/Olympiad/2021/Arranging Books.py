def ArrangeBooks(shelf):
    shelflist = []
    for i in shelf:
        shelflist.append(i)

    counter = 0
    for index, letters in enumerate(shelflist):
        if letters == "M" or letters == "S":
            sublist = shelflist[index:]
            for index2, elements in enumerate(sublist):
                if elements == "L":
                    counter += 1
                else:
                    continue
                if index2 == len(sublist):
                    subsublist = sublist[index2:]
                    for index3, elements2 in enumerate(sublist):
                        if elements2 == "S":
                            counter += 1
                        else:
                            continue


print(ArrangeBooks("LMMMSLL"))
