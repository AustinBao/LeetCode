import unittest
from unittest import TestCase


def sunflowers(size, garden):
    if iscolumbvalid(findyaxis(size, garden)) and isrowvalid(garden):
        return garden
    else:
        newgarden = rotatecounterclockwise(size, garden)
        return sunflowers(size, newgarden)


def rotatecounterclockwise(size, yaxis):
    newgarden = []
    for columb in range(size - 1, -1, -1):
        curr = []
        for rows in yaxis:
            curr.append(rows[columb])
        newgarden.append(curr)
    return newgarden


def findyaxis(size, garden):
    yaxis = []
    for columb in range(0, size):
        curr = []
        for rows in garden:
            curr.append(str(rows[columb]))
        yaxis.append(curr)
    return yaxis

 # Seems like isrowvalid and iscolumbvalid have the same code, you could just rename the method and its
 # variables a little so that you can just reuse them
def isrowvalid(xaxislist):
    for rows in xaxislist:
        previous = rows[0]
        for flowers in rows:
            if previous > flowers:
                return False
    return True


def iscolumbvalid(yaxislist):
    for columbs in yaxislist:
        previous = columbs[0]
        for flowers in columbs:
            if previous > flowers:
                return False
    return True


# Doesnt work for ALL cases since in the question, we know we are guaranteed a corrct situation.
# therefore we cant just plug in any number we want as we dont know if it has any correct orientation.

class TestSunflower(TestCase):

    def test_2_by_2_correct(self):
        garden = [[1, 3],
                  [2, 7]]
        self.assertEqual(first=[[1, 3], [2, 7]], second=sunflowers(2, garden))

    def test_2_by_2_incorrect(self):
        garden = [[8, 2],
                  [7, 1]]
        self.assertEqual(first=[[1, 7], [2, 8]], second=sunflowers(2, garden))

    def test_3_by_3_correct(self):
        garden = [[1, 3, 5],
                  [2, 7, 8],
                  [3, 5, 9]]
        self.assertEqual(first=garden, second=sunflowers(3, garden))

    def test_3_by_3_incorrect(self):
        garden = [[3, 7, 9],
                  [2, 5, 6],
                  [1, 3, 4]]
        self.assertEqual(first=[[1, 2, 3], [3, 5, 7], [4, 6, 9]], second=sunflowers(3, garden))


if __name__ == '__main__':
    unittest.main()


# print(findyaxis(3, [[1, 2, 3],
#                     [4, 5, 6],
#                     [7, 8, 9]]))

# print(rotatecounterclockwise(3, [[1, 2, 3],
#                                  [4, 5, 6],
#                                  [7, 8, 9]]))

# print(rotatecounterclockwise(3, [[3, 6, 9],
#                                  [2, 5, 8],
#                                  [1, 4, 7]]))

# print(rotatecounterclockwise(3, [[9, 8, 7],
#                                  [6, 5, 4],
#                                  [3, 2, 1]]))

# print(rotatecounterclockwise(3, [[7, 4, 1],
#                                  [8, 5, 2],
#                                  [9, 6, 3]]))
#

# print(rotatecounterclockwise(3, [[1, 4, 7],
#                                  [2, 5, 8],
#                                  [3, 6, 9]]))

