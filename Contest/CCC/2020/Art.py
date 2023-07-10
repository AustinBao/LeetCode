# https://www.cemc.uwaterloo.ca/contests/computing/2020/ccc/juniorEF.pdf

import unittest
from unittest import TestCase


def artFrame(num_dots, dot_cords):
    x_cord = []
    y_cord = []
    for cords in dot_cords:
        if cords[0] == 0 or cords[1] == 0:
            return "canvas out of bounds"
        else:
            x_cord.append(cords[0])
            y_cord.append(cords[1])

    curr_x_small = min(x_cord)
    curr_y_small = min(y_cord)

    curr_x_big = max(x_cord)
    curr_y_big = max(y_cord)

    return [curr_x_small - 1, curr_y_small - 1], [curr_x_big + 1, curr_y_big + 1]


class TestArtFrame(TestCase):

    def test_normalexample1(self):
        self.assertEqual(first=([23, 9], [65, 79]), second=artFrame(5, [[44, 62], [34, 69], [24, 78], [42, 44], [64, 10]]))

    def test_outofboundsex1(self):
        self.assertEqual(first="canvas out of bounds", second=artFrame(3, [[0, 0], [100, 10], [2, 3]]))

    def test_outofboundsex2(self):
        self.assertEqual(first="canvas out of bounds", second=artFrame(3, [[1, 0], [100, 10], [2, 3]]))

    def test_outofboundsex3(self):
        self.assertEqual(first="canvas out of bounds", second=artFrame(3, [[0, 1], [100, 10], [2, 3]]))

    def test_smallestamountofdots(self):
        self.assertEqual(first=([0, 0], [3, 3]), second=artFrame(2, [[1, 1], [2, 2]]))


if __name__ == '__main__':
    unittest.main()
