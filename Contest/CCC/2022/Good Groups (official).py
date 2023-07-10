import unittest
from unittest import TestCase


def goodGroups(num_tog, tog, num_sep, sep, num_group, groups):
    counter = {}
    for i in tog:
        counter[str(i)] = True
    for j in sep:
        counter[str(j)] = True

    for indi in groups:
        for elements in tog:
            if check_if_together(indi, elements) is False:
                counter[str(elements)] = False
            else:
                continue

        for elements2 in sep:
            if check_if_separate(indi, elements2) is False:
                counter[str(elements2)] = False
            else:
                continue

    finaloutput = 0
    for keys in counter:
        if counter[keys] == False:
            finaloutput += 1

    return finaloutput


def check_if_together(curr_group, elements):
    for index, member in enumerate(elements):
        if member in curr_group:
            if index == 0:
                if elements[1] not in curr_group:
                    return False
            else:
                if elements[0] not in curr_group:
                    return False
    return True


def check_if_separate(curr_group, elements):
    for index, member in enumerate(elements):
        if member in curr_group:
            if index == 0:
                if elements[1] in curr_group:
                    return False
            else:
                if elements[0] in curr_group:
                    return False
    return True


class TestGroups(TestCase):

    def test_fromcontest(self):
        self.assertEqual(first=3, second=goodGroups(3, [["A", "B"], ["G", "L"], ["J", "K"]], 2, [["D", "F"], ["D", "G"]], 4,
                 [["A", "C", "G"], ["B", "D", "F"], ["E", "H", "I"], ["J", "K", "L"]]))

    def test_no_separate(self):
        self.assertEqual(first=0, second=goodGroups(1, [["A", "B"]], 0, [], 2, [["A", "B", "G"], ["V", "D", "F"]]))

    def test_no_together(self):
        self.assertEqual(first=1, second=goodGroups(0, [], 0, [["A", "B"]], 2, [["A", "B", "G"], ["V", "D", "F"]]))

    def test_perfect_groups(self):
        self.assertEqual(first=0, second=goodGroups(0, [], 0, [], 2, [["A", "B", "G"], ["V", "D", "F"]]))


if __name__ == '__main__':
    unittest.main()