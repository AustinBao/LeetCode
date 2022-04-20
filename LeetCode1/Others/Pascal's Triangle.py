def pascal(rows):
    counter = 0
    constructed_triangle = [[1]]
    blist = [1]

    while rows-1 > counter:
        constructed_triangle.append(trianglemaker(blist))
        blist = trianglemaker(blist)
        counter += 1
    return constructed_triangle


def trianglemaker(alist):
    newrow = []
    alist.insert(0,0)
    alist.insert(len(alist),0)

    for elements in range(0, len(alist) - 1):
        one_ahead = elements + 1
        newrow.append(alist[elements] + alist[one_ahead])
        newrow = [x for x in newrow if x != 0]
    return newrow


print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
