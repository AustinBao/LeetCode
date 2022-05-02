def poolgenerator(n: int, numberoftrees: int, row, column):
    dimensions = sizeofyard(n)
    locationoftree(dimensions, row, column)
    return dimensions


def locationoftree(dimensions, x, y):
    x_index = x - 1
    y_index = y - 1
    return dimensions[x_index].append("T")


def sizeofyard(size):
    dimensions = []
    for rows in range(0, size):
        for columns in range(0, size):
            dimensions.append([])
    return dimensions


print(poolgenerator(3, 1, 1, 0))
