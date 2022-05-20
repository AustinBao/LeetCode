def squarePool(size, num_trees, coord_trees):
    grid = []
    for x in range(1, size+1):
        for y in range(1, size+1):
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


def ceilingandright(point, ceilingpoint, rightpoint):
    largestcubesize = []
    largestcubesize.append(rightpoint[0] - point[0] - 1)
    largestcubesize.append(point[1] - ceilingpoint[1])
    return min(largestcubesize)


def checkMaxSquareOnRight(point, trees, size):
    treesToTheRight = []
    for tree in trees:
        if tree[0] >= point[0]:
            treesToTheRight.append(tree)

    maxDistanceToRight = size - point[0] + 1
    startX = point[0]
    startY = 1
    endY = size

    for poolSize in range(maxDistanceToRight, 0, -1):
        for startY in range(1, endY - poolSize + 1 + 1):
            if doesSquareFit(poolSize, startX, startY, treesToTheRight):
                return poolSize

    return 0


def doesSquareFit(squareSize, startX, startY, trees):
    endX = startX + squareSize - 1
    endY = startY + squareSize - 1
    for tree in trees:
        treeX = tree[0]
        treeY = tree[1]
        if (startX <= treeX <= endX) and (startY <= treeY <= endY):
            return False
    return True


print(checkMaxSquareOnRight([2, 4], [[4, 2]], 7))

print(checkMaxSquareOnRight([2, 4], [[4, 2], [6, 3], [5, 5], [5, 6], [2, 4]], 7))

print(checkMaxSquareOnRight([2, 4], [[6, 3], [5, 5], [5, 6], [1, 4]], 7))

print(checkMaxSquareOnRight([2, 4], [[3, 4], [6, 3], [5, 5], [5, 6], [1, 4]], 7))

print(checkMaxSquareOnRight([2, 4], [[3, 4], [3, 6], [4, 2], [6, 3], [5, 5], [5, 6], [1, 4]], 7))

#print(squarePool(4, 2, [[2, 2], [3, 2]]))
#print(squarePool(5, 1, [[2, 4]]))
#print(squarePool(15, 8, [[4, 7], [4, 1], [14, 11], [10, 6], [13, 4], [4, 10], [10, 3], [9, 14]]))


