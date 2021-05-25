import unittest
from unittest import TestCase


def fizzbuzz(n):
    strlist = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            strlist.append("FizzBuzz")
        elif i % 3 == 0:
            strlist.append("Fizz")
        elif i % 5 == 0:
            strlist.append("Buzz")
        else:
            strlist.append(str(i))
    return strlist


class testFizz(TestCase):
    def onlyThree(self):
        mynum = 3
        self.assertEqual(first=["1", "2", "Fizz"], second=fizzbuzz(mynum))

if __name__ == '__main__':
    unittest.main()