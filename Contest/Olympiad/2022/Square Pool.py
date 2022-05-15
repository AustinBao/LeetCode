# def squarePool(size, num_trees, coord_trees):
#     grid = []
#     for x in range(1, size + 1):
#         for y in range(1, size + 1):
#             grid.append([x, y])
#
#     sizes = set()
#     for poolTile in grid:
#         startX = poolTile[0]
#         startY = poolTile[1]
#         size_to_increase = 1
#         blocked = False
#         while not blocked:
#             if (startX + size_to_increase > size) or (startY + size_to_increase > size):
#                 break
#             for tree_coord in coord_trees:
#                 if poolTile == tree_coord:
#                     blocked = True
#                     break
#                 if isTreeHit(poolTile, size_to_increase, tree_coord):
#                     blocked = True
#                     break
#             if not blocked:
#                 size_to_increase += 1
#         sizes.add(size_to_increase)
#
#     return max(sizes)

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
    for yincrease in range(0, xscale[k] + 1):
        for xincrease in range(1, xscale[k] + 1):
            possiblesquare.append([point[0] + yincrease, point[1] + xincrease])
            print(possiblesquare)
            if possiblesquare.__contains__(other_tree_coords):
                return possiblesquare


print(ceilingandright([8, 15], [[23, 30], [3, 28], [19, 19], [12, 21], [12, 9], [21, 3], [5, 5]]))
