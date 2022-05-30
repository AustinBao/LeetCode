# https://www.cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf


import unittest
from unittest import TestCase


def ColdCompress(lines, message):
    if lines == 0:
        return ""

    msglist = []
    for word_index in range(0, lines):
        for letters in message[word_index]:
            msglist.append(letters)

    counter = 0
    symbol_num = {}
    previous = msglist[0]

    for index, elements in enumerate(msglist):
        if previous == elements:
            counter += 1
            continue
        elif previous != elements:
            symbol_num[previous] = counter
            previous = elements
            counter = 1

    final_output = []
    left_len = 0
    for key in symbol_num:
        final_output.append(str(symbol_num[key]))
        final_output.append(key)
        left_len += symbol_num[key]

    left_symbol = msglist[left_len]
    len_of_left = len(msglist) - left_len

    final_output.append(str(len_of_left))
    final_output.append(left_symbol)

    str1 = " "
    return str1.join(final_output)


print(ColdCompress(1, ["+++===!!!!"]))
print(ColdCompress(2, ["+++===!!!!", "+++"]))


class TestCompress(TestCase):

    def test_nothing(self):
        self.assertEqual(first="", second=ColdCompress(0, []))

    def test_one_single_symbol(self):
        self.assertEqual(first="1 +", second=ColdCompress(1, ["+"]))

    def test_one_multiple_symbol(self):
        self.assertEqual(first="3 +", second=ColdCompress(1, ["+++"]))

    def test_single_first_symbol(self):
        self.assertEqual(first="1 : 2 0 1 + 2 -", second=ColdCompress(1, [":00+--"]))

    def test_example1(self):
        self.assertEqual(first="3 + 3 = 4 !", second=ColdCompress(1, ["+++===!!!!"]))

    def test_same_symbol_first_and_end(self):
        self.assertEqual(first="3 + 3 = 4 ! 3 +", second=ColdCompress(1, ["+++===!!!!+++"]))

    def test_alternating_symbols(self):
        self.assertEqual(first="1 + 1 = 1 +", second=ColdCompress(1, ["+=+"]))

    def test_example2(self):
        self.assertEqual(first="6 7 6 . 12 T", second=ColdCompress(1, ["777777......TTTTTTTTTTTT"]))

    def test_more_than_one_line(self):
        self.assertEqual(first="3 + 3 = 4 ! 6 7 6 . 12 T 1 ( 2 A 2 B 1 C 1 ) 1 3 1 . 1 1 1 4 1 1 4 5", second=ColdCompress(4, ["+++===!!!!", "777777......TTTTTTTTTTTT", "(AABBC)", "3.1415555"]))

    def test_one_multiple_symbol_twice(self):
        self.assertEqual(first="3 + 2 +", second=ColdCompress(2, ["+++" , "++"]))


if __name__ == '__main__':
    unittest.main()
