# https://www.cemc.uwaterloo.ca/contests/computing/2022/ccc/juniorEF.pdf

import unittest
from unittest import TestCase


def fergusonball(separate_players, scores_and_fouls):
    if separate_players == 0:
        return "0-"

    sublist = []
    for nums in range(0, len(scores_and_fouls), 2):
        sublist.append(scores_and_fouls[nums:nums + 2])

    star_players = []
    for i in sublist:
        for j in range(0, len(sublist[0]) - 1):
            star_players.append((i[j] * 5) - (i[j + 1] * 3))

    counter = 0
    for items in star_players:
        if items > 40:
            counter += 1

    if counter == separate_players:
        return "{}+".format(counter)
    else:
        return "{}-".format(counter)


class TestFerguson(TestCase):

    def test_normalamountplayers_starteam(self):
        self.assertEqual(first="4+", second=fergusonball(4, [12, 4, 10, 3, 9, 1, 18, 2]))

    def test_normalamountplayers_nostar(self):
        self.assertEqual(first="0-", second=fergusonball(4, [2, 1, 10, 7, 9, 8, 17, 16]))

    def test_noplayers_nostar(self):
        self.assertEqual(first="0-", second=fergusonball(0, []))

    def test_oneplayer_star(self):
        self.assertEqual(first="1+", second=fergusonball(1, [9, 1]))

    def test_oneplayer_nostar(self):
        self.assertEqual(first="0-", second=fergusonball(1, [1, 0]))


if __name__ == '__main__':
    unittest.main()
