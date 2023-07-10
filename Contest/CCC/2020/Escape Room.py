def escapeRoom(row, columb, cordinates):
    plane = []
    for x in range(1, row + 1):
        for y in range(1, columb + 1):
            plane.append((x, y))

    together = [0] * (len(cordinates) + len(plane))
    together[::2] = cordinates
    together[1::2] = plane

    x,y = together[-1]
    for cords in range(len(together), -1, -2):
        for points in range(len(together) - 1, 0, -2):
            if x * y == together[points]:
                x,y = together[points + 1]
    return together


print(escapeRoom(3, 4, [3, 10, 8, 14, 1, 11, 12, 12, 6, 2, 3, 9]))
