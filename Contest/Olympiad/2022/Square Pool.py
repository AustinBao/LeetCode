def squarePool(size, num_trees, coord_trees):
    grid = []
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            grid.append([x, y])

    sizes = set()
    for poolTile in grid:
        startX = poolTile[0]
        startY = poolTile[1]
        size_to_increase = 1
        blocked = False
        while not blocked:
            if (startX + size_to_increase > size) or (startY + size_to_increase > size):
                break
            for tree_coord in coord_trees:
                if poolTile == tree_coord:
                    blocked = True
                    break
                if isTreeHit(poolTile, size_to_increase, tree_coord):
                    blocked = True
                    break
            if not blocked:
                size_to_increase += 1
        sizes.add(size_to_increase)

    return max(sizes)


def isTreeHit(poolTile, size_increase, tree_coord):
    startX = poolTile[0]
    startY = poolTile[1]
    filled_coords = []
    for i in range(startX, startX + size_increase + 1):
        for j in range(startY, startY + size_increase + 1):
            filled_coords.append([i, j])
    return filled_coords.__contains__(tree_coord)


def checkMaxSquareOnTop(point, trees, size):
    treesToTheTop = []
    for tree in trees:
        if tree[1] <= point[1]:
            treesToTheTop.append(tree)

    startY = point[1]
    size_of_initial_square = point[1]
    for size_of_square in range(size_of_initial_square, 0, -1):
        for x in range(1, size + 1):
            if x + x + size_of_square - 1 > size:
                continue
            if doesSquareFit(size_of_square, x, startY, treesToTheTop):
                return size_of_square
    return 0


def doesSquareFit(size_of_square, startX, startY, treesToTheTop):
    endX = startX + size_of_square - 1
    highestY = startY - size_of_square + 1
    for tree in treesToTheTop:
        treeX = tree[0]
        treeY = tree[1]
        if (startX <= treeX <= endX) and ( highestY<= treeY <= startY):
            return False
    return True


print(checkMaxSquareOnTop([2, 5], [], 8))

print(checkMaxSquareOnTop([2, 5], [[3,3], [6,3]], 8))

print(checkMaxSquareOnTop([2, 5], [[3,3], [6,3], [2,4], [4,4], [7,4]], 8))

print(checkMaxSquareOnTop([2, 5], [[3,2], [6,4]], 8))

print(checkMaxSquareOnTop([2, 5], [[3,3], [6,2]], 8))




