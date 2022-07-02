def sunflowers(size, garden):
    previousheight = garden[0][0]
    for rows in garden:
        if rows[0] >= previousheight:
            previousheight = rows[0]
            continue
        else:
            return turn90degreecounterclockwise(size, garden)
    return garden


def turn90degreecounterclockwise(n, garden):
    yaxis = []
    i = 0
    for columb in range(0, n):
        curr = ""
        for rows in garden:
            curr += str(rows[columb])
        yaxis.append(curr)
    return garden, yaxis


# print(sunflowers(2, [[1, 3],
#                      [2, 4]]))
#
# print(sunflowers(3, [[3, 3, 9],
#                      [2, 4, 6],
#                      [5, 6, 7]]))

print(sunflowers(3, [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8]]))
