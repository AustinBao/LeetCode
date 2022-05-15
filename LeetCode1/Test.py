def ceilingandright(point, other_tree_coords):
    xscale = []
    yscale = []

    for trees in other_tree_coords:
        xdiff = trees[0] - point[0] - 1
        if xdiff <= 0:
            continue
        ydiff = point[1] - trees[1] - 1
        xscale.append(xdiff)
        yscale.append(ydiff)

    xscale.sort()
    xscale.reverse()
    yscale.sort()
    yscale.reverse()

    k = 0
    possiblesquare = []
    above_y_value = 0
    ceiling = []
    for yincrease in range(0, xscale[k] + 1):
        for xincrease in range(1, xscale[k] + 1):
            possiblesquare.append([point[1] + xincrease, point[0] + yincrease])
            above_y_value = xscale[k]

    for cords in possiblesquare:
        for trees in other_tree_coords:
            if cords == trees:
                cordinate_above_y = point[1] - above_y_value
                ceiling = trees[1] - cordinate_above_y

    if ceiling > 0:
        ceiling * (-1)

    for things in yscale:
        if ceiling == things:
            pass
    return ceiling


print(ceilingandright([8, 15], [[23, 30], [3, 28], [19, 19], [12, 21], [12, 9], [21, 3], [5, 5]]))
