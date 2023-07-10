def flipper(instructions):
    grid = [[1, 2],
            [3, 4]]

    for letter in instructions:
        if letter == "H":
            grid.reverse()
        if letter == "V":
            grid[0].reverse()
            grid[1].reverse()

    return grid


print(flipper("VHHHV"))
