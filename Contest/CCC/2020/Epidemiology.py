# https://www.cemc.uwaterloo.ca/contests/computing/2020/ccc/juniorEF.pdf

import unittest
from unittest import TestCase


def epidemiology(have_disease, day_0, rate_of_increase):
    if have_disease == day_0:
        return day_0

    days = 0
    list_of_infected = []
    j = 0
    while sum(list_of_infected) <= have_disease:
        list_of_infected.append(day_0 * (rate_of_increase ** j))
        j += 1
        days += 1

    return days - 1


class TestEpidemiology(TestCase):

    def test_normalexample1(self):
        self.assertEqual(first=4, second=epidemiology(750, 1, 5))

    def test_normalexample2(self):
        self.assertEqual(first=5, second=epidemiology(10, 2, 1))

    def test_healthyWorld(self):
        self.assertEqual(first=0, second=epidemiology(0, 0, 0))

    def test_havedisease_equal_day0(self):
        self.assertEqual(first=300, second=epidemiology(300, 300, 4))


if __name__ == '__main__':
    unittest.main()
