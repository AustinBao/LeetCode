# https://www.cemc.uwaterloo.ca/contests/computing/2021/ccc/juniorEF.pdf

import unittest
from unittest import TestCase


def silentAuction(numofbids, nameandpricelist):
    prices = []
    names = []
    for i in range(0, len(nameandpricelist) - numofbids):
        prices.append(nameandpricelist[(i * 2) + 1])
        names.append(nameandpricelist[i * 2])

    curr_max = 0
    person = ""
    for index, value in enumerate(prices):
        if curr_max < value:
            curr_max = value
            person = names[index]
    return person


class TestSilentAuction(TestCase):

    def test_oneperson(self):
        self.assertEqual(first="Jack", second=silentAuction(1, ["Jack", 10]))

    def test_normalexample(self):
        self.assertEqual(first="Jerry", second=silentAuction(6, ["Austin", 700, "Jerry", 900, "Ahmed", 40, "Suzanne", 500, "Ivona", 600, "Jordan", 600]))

    def test_samemoney(self):
        self.assertEqual(first="Austin", second=silentAuction(2, ["Austin", 900, "Jerry", 900]))

    def test_nomoney(self):
        self.assertEqual(first="", second=silentAuction(1, ["Austin", 0]))


if __name__ == '__main__':
    unittest.main()
