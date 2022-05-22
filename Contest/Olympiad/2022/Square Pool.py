import unittest
from unittest import TestCase


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
            if doesSquareFitRight(poolSize, startX, startY, treesToTheRight):
                return poolSize

    return 0


def doesSquareFitRight(squareSize, startX, startY, trees):
    endX = startX + squareSize - 1
    endY = startY + squareSize - 1
    for tree in trees:
        treeX = tree[0]
        treeY = tree[1]
        if (startX <= treeX <= endX) and (startY <= treeY <= endY):
            return False
    return True


def checkMaxSquareOnLeft(point, trees, size):
    treesToTheLeft = []
    for tree in trees:
        if tree[0] <= point[0]:
            treesToTheLeft.append(tree)

    endX = point[0]

    for size_of_pool in range(endX, 0, -1):
        for startY in range(1, size + 1):
            if startY + size_of_pool - 1 > size:
                break
            if doesSquareFitLeft(size_of_pool, endX, startY, treesToTheLeft):
                return size_of_pool

    return 0


def doesSquareFitLeft(size_of_pool, endX, startY, trees):
    startX = endX - size_of_pool + 1
    endY = startY + size_of_pool - 1
    for tree in trees:
        treeX = tree[0]
        treeY = tree[1]
        if (startX <= treeX <= endX) and (startY <= treeY <= endY):
            return False
    return True


def checkMaxSquareOnTop(point, trees, size):
    treesToTheTop = []
    for tree in trees:
        if tree[1] <= point[1]:
            treesToTheTop.append(tree)

    startY = point[1]
    size_of_initial_square = point[1]
    for size_of_square in range(size_of_initial_square, 0, -1):
        for x in range(1, size + 1):
            if x + size_of_square - 1 > size:
                break
            if doesSquareFitAbove(size_of_square, x, startY, treesToTheTop):
                return size_of_square
    return 0


def doesSquareFitAbove(size_of_initial_square, startX, startY, treesToTheTop):
    endX = startX + size_of_initial_square - 1
    highestY = startY - size_of_initial_square + 1
    for tree in treesToTheTop:
        treeX = tree[0]
        treeY = tree[1]
        if (startX <= treeX <= endX) and (highestY <= treeY <= startY):
            return False
    return True


def checkMaxSquareBelow(point, trees, size):
    treesToTheBottom = []
    for tree in trees:
        if tree[1] >= point[1]:
            treesToTheBottom.append(tree)

    startY = point[1]
    size_of_initial_square = size - point[1] + 1

    for size_of_square in range(size_of_initial_square, 0, -1):
        for x in range(1, size + 1):
            if x + size_of_square - 1 > size:
                break
            if doesSquareFitUnder(size_of_square, x, startY, treesToTheBottom):
                return size_of_square
    return 0


def doesSquareFitUnder(size_of_initial_square, startX, startY, treesToTheBottom):
    endX = startX + size_of_initial_square - 1
    LowestY = startY + size_of_initial_square - 1
    for tree in treesToTheBottom:
        treeX = tree[0]
        treeY = tree[1]
        if (startX <= treeX <= endX) and (startY <= treeY <= LowestY):
            return False
    return True


def squarePool(size, num_of_trees, tree_cords):
    list_of_all_square_sizes = []
    if num_of_trees == 0:
        list_of_all_square_sizes.append(size)

    pointstotheleft = []
    pointstotheright = []
    pointstothetop = []
    pointstothebottom = []

    grid = []
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            grid.append([x, y])

    for trees in tree_cords:
        x = trees[0]
        y = trees[1]
        # top left
        if x - 1 < 1 and y - 1 < 1:
            pointstotheright.append([x + 1, y])
            pointstothebottom.append([x, y + 1])
        # bottom left
        if x - 1 < 1 and y + 1 > size:
            pointstotheright.append([x + 1, y])
            pointstothetop.append([x, y - 1])
        # top right
        if x + 1 > size and y - 1 < 1:
            pointstotheleft.append([x - 1, y])
            pointstothebottom.append([x, y + 1])
        # bottom right
        if x + 1 > size and y + 1 > size:
            pointstotheleft.append([x - 1, y])
            pointstothetop.append([x, y - 1])
        # everything else
        else:
            pointstotheleft.append([x - 1, y])
            pointstotheright.append([x + 1, y])
            pointstothetop.append([x, y - 1])
            pointstothebottom.append([x, y + 1])

    for left in pointstotheleft:
        list_of_all_square_sizes.append(checkMaxSquareOnLeft(left, tree_cords, size))

    for right in pointstotheright:
        list_of_all_square_sizes.append(checkMaxSquareOnRight(right, tree_cords, size))

    for top in pointstothetop:
        list_of_all_square_sizes.append(checkMaxSquareOnTop(top, tree_cords, size))

    for bot in pointstothebottom:
        list_of_all_square_sizes.append(checkMaxSquareBelow(bot, tree_cords, size))

    return max(list_of_all_square_sizes)


class TestMaxSqareUnder(TestCase):

    def test_no_trees(self):
        self.assertEqual(first=4, second=checkMaxSquareBelow([2, 5], [], 8))

    def test_not_touching_point(self):
        self.assertEqual(first=4, second=checkMaxSquareBelow([2, 5], [[1, 6], [2, 6], [3, 6], [4, 6]], 8))

    def test_normal2by2(self):
        self.assertEqual(first=2, second=checkMaxSquareBelow([2, 5], [[2, 6], [5, 7], [7, 6]], 8))

    def test_barrier(self):
        self.assertEqual(first=1, second=checkMaxSquareBelow([2, 5], [[2, 6], [4, 6], [6, 6], [8, 6]], 8))


class TestMaxSqareAbove(TestCase):

    def test_no_trees(self):
        self.assertEqual(first=5, second=checkMaxSquareOnTop([2, 5], [], 8))

    def test_not_touching_point(self):
        self.assertEqual(first=5, second=checkMaxSquareOnTop([2, 5], [[1, 3], [3, 3]], 8))

    def test_barrier(self):
        self.assertEqual(first=1, second=checkMaxSquareOnTop([2, 5], [[7, 4], [5, 4], [3, 4], [1, 4]], 8))

    def test_square_above_barrier(self):
        self.assertEqual(first=3, second=checkMaxSquareOnTop([2, 3], [[7, 4], [5, 4], [3, 4], [1, 4]], 8))


class TestMaxSqareRight(TestCase):

    def test_normal(self):
        self.assertEqual(first=5, second=checkMaxSquareOnRight([2, 4], [[4, 2]], 7))

    def test_more_trees(self):
        self.assertEqual(first=3, second=checkMaxSquareOnRight([2, 4], [[4, 2], [6, 3], [5, 5], [5, 6], [2, 4]], 7))


class TestMaxSqareLeft(TestCase):

    def test_no_trees(self):
        self.assertEqual(first=6, second=checkMaxSquareOnLeft([6, 4], [], 8))

    def test_one_tree_halved(self):
        self.assertEqual(first=4, second=checkMaxSquareOnLeft([6, 4], [[3, 4]], 8))

    def test_barrier(self):
        self.assertEqual(first=1, second=checkMaxSquareOnLeft([6, 4], [[5, 2], [5, 4], [5, 6], [5, 8]], 8))


class TestPoolSize(TestCase):

    def test_no_trees(self):
        self.assertEqual(first=8, second=squarePool(8, 0, []))

    def test_trees_in_corners(self):
        self.assertEqual(first=6, second=squarePool(8, 4, [[1, 1], [1, 8], [8, 1], [8, 8]]))

    def test_points_touching_the_side(self):
        self.assertEqual(first=6, second=squarePool(8, 4, [[1, 4], [4, 8], [8, 4], [4, 1]]))

    def test_example1_from_contest(self):
        self.assertEqual(first=3, second=squarePool(5, 1, [[2, 4]]))

    def test_example2_from_contest(self):
        self.assertEqual(first=7, second=squarePool(15, 8,
                                                    [[4, 7], [4, 1], [14, 11], [10, 6], [13, 4], [4, 10], [10, 3],
                                                     [9, 14]]))


if __name__ == '__main__':
    unittest.main()
