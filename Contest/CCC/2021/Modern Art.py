# https://www.cemc.uwaterloo.ca/contests/computing/2021/ccc/juniorEF.pdf


def modernArt(rows, columbs, num_brushes, brushes):
    table = []
    for i in range(0, rows):
        new = []
        for j in range(0, columbs):
            new.append("B")
        table.append(new)

    final = []
    for instructions in brushes:
        if instructions == brushes[-1]:
            if instructions[0] == "R":
                final.append(r_brush(table, instructions[1]))
            if instructions[0] == "C":
                final.append(c_brush(table, instructions[1], rows))
        else:
            if instructions[0] == "R":
                table = r_brush(table, instructions[1])
            if instructions[0] == "C":
                table = c_brush(table, instructions[1], rows)

    counter = 0
    for rows in table:
        for elements in rows:
            if elements == "G":
                counter += 1

    return counter


def c_brush(table, specific_columbs, rows):
    for rows in table:
        if rows[specific_columbs - 1] == "B":
            rows[specific_columbs - 1] = "G"
        else:
            rows[specific_columbs - 1] = "B"

    return table


def r_brush(table, specific_row):
    temp = []
    for i in table[specific_row - 1]:
        if i == "G":
            temp.append("B")
        elif i == "B":
            temp.append("G")

    table[specific_row - 1] = temp

    return table


print(modernArt(3, 3, 2, [["R", 1], ["C", 1]]))

print(modernArt(4, 5, 7, [["R", 3], ["C", 1], ["C", 2], ["R", 2], ["R", 2], ["C", 1], ["R", 4]]))
