# https://www.cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf


import unittest
from unittest import TestCase


def ColdCompress(lines, message):
    finaloutput = []
    numlist = []
    symbollist = []
    remainder = []
    counter = 0

    # edge case for when there are no messages
    if lines == 0:
        return ""

    # Edge case for when there is only one symbol
    acc = message[0]
    if acc == len(acc) * acc[0]:
        for num_of_repeating_msg in range(0, lines):
            finaloutput.append(str(len(message[num_of_repeating_msg])))
            finaloutput.append(" ")
            finaloutput.append(acc[0])
            finaloutput.append(" ")
        finaloutput.pop()
        msg1 = ""
        return msg1.join(finaloutput)

    msglist = []
    for strs in message:
        for letters in strs:
            msglist.append(letters)

    previous = msglist[0]
    for index, character in enumerate(msglist):
        if previous == character:
            counter += 1
            continue
        if previous != character:
            symbollist.append(previous)
            numlist.append(counter)
            counter = 1
            previous = character
        if msglist[-1] == character:
            remainder = msglist[index::]
            numlist.append(len(remainder))
            symbollist.append(remainder[0])

    j = 0
    for i in range(0, len(numlist)):
        finaloutput.append(str(numlist[i]))
        finaloutput.append(symbollist[j])
        j += 1

    msgstr = " "
    return msgstr.join(finaloutput)


class TestCompress(TestCase):

    def test_nothing(self):
        self.assertEqual(first="", second=ColdCompress(0, []))

    def test_one_single_symbol(self):
        self.assertEqual(first="1 +", second=ColdCompress(1, ["+"]))

    def test_one_multiple_symbol(self):
        self.assertEqual(first="3 +", second=ColdCompress(1, ["+++"]))

    def test_one_multiple_symbol_twice(self):
        self.assertEqual(first="3 + 2 +", second=ColdCompress(2, ["+++", "++"]))

    def test_example1(self):
        self.assertEqual(first="3 + 3 = 4 !", second=ColdCompress(1, ["+++===!!!!"]))

    def test_same_symbol_first_and_end(self):
        self.assertEqual(first="3 + 3 = 4 ! 3 +", second=ColdCompress(1, ["+++===!!!!+++"]))

    def test_alternating_symbols(self):
        self.assertEqual(first="1 + 1 = 1 +", second=ColdCompress(1, ["+=+"]))

    def test_example2(self):
        self.assertEqual(first="6 7 6 . 12 T", second=ColdCompress(1, ["777777......TTTTTTTTTTTT"]))

    def test_more_than_one_line(self):
        self.assertEqual(first="3 + 3 = 4 ! 6 7 6 . 12 T 1 ( 2 A 2 B 1 C 1 ) 1 3 1 . 1 1 1 4 1 1 4 5",
                         second=ColdCompress(4, ["+++===!!!!", "777777......TTTTTTTTTTTT", "(AABBC)", "3.1415555"]))

    def test_single_first_symbol(self):
        self.assertEqual(first="1 : 2 0 1 + 2 -", second=ColdCompress(1, [":00+--"]))


if __name__ == '__main__':
    unittest.main()
