# https://www.cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf


import unittest
from unittest import TestCase


def Decompress(lines, secretcode):
    message = []
    numberoftimes = []
    for i in secretcode:
        message.append(i[-1])
        if len(i) == 4:
            numberoftimes.append(i[:2:])
        else:
            numberoftimes.append(i[0])

    decoded = []
    j = 0
    for num in numberoftimes:
        for things in range(0, int(num)):
            decoded.append(message[j])
        decoded.append(" ")
        j += 1

    if lines == 0:
        return ""
    else:
        # pop to get rid of space after last msg
        decoded.pop()

    finalstr = ""
    return finalstr.join(decoded)


print(Decompress(4, ["9 +", "3 -", "12 A", "2 X"]))


class TestDecompress(TestCase):

    def test_example(self):
        self.assertEqual(first="+++++++++ --- AAAAAAAAAAAA XX", second=Decompress(4, ["9 +", "3 -", "12 A", "2 X"]))

    def test_nothing(self):
        self.assertEqual(first="", second=Decompress(0, []))

    def test_onemsg(self):
        self.assertEqual(first="]]]]]]", second=Decompress(1, ["6 ]"]))




if __name__ == '__main__':
    unittest.main()