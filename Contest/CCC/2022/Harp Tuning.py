# https://www.cemc.uwaterloo.ca/contests/computing/2022/ccc/juniorEF.pdf

import unittest
from unittest import TestCase


def harpTuning(instructions):
    tunedlist = []
    for elements in instructions:
        if elements == "+":
            tunedlist.append("tighten")
            continue
        if elements == "-":
            tunedlist.append("loosen")
            continue
        tunedlist.append(elements)

    substrings = ""
    listofstrings = []
    for i in tunedlist:
        if i == "tighten" or i == "loosen":
            listofstrings.append(substrings)
            substrings = ""
        if i.isalpha():
            if len(i) == 1:
                substrings += i
        else:
            continue

    listoftuning = []
    for i in tunedlist:
        if i == "tighten":
            listoftuning.append("tighten")
        if i == "loosen":
            listoftuning.append("loosen")

    listofnumbers = []
    for i in tunedlist:
        if i.isdigit():
            listofnumbers.append(i)
        else:
            continue

    final = []
    for index in range(0, len(listofstrings)):
        final.append("{} {} {}".format(listofstrings[index], listoftuning[index], listofnumbers[index]))

    str1 = " "
    return str1.join(final)


class TestHarpTune(TestCase):

    def test_tune4times(self):
        self.assertEqual(first="ABD tighten 4 FCD loosen 5 YUWZX tighten 1 TRADOP loosen 2",
                         second=harpTuning("ABD+4FCD-5YUWZX+1TRADOP-2"))

    def test_tune1time(self):
        self.assertEqual(first="FVB loosen 7", second=harpTuning("FVB-7"))

    def test_tunenothing(self):
        self.assertEqual(first="", second=harpTuning(""))


if __name__ == '__main__':
    unittest.main()
