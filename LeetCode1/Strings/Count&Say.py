import unittest
from unittest import TestCase

def split(inputList):
    outerList = []
    maxValueOfJ = -1
    if len(inputList) == 1:
        return [inputList]

    for i in range(len(inputList)):
        if i > maxValueOfJ:
            innerList = [inputList[i]]
            for j in range(i + 1, len(inputList)):
                if inputList[i] == inputList[j]:
                    innerList.append(inputList[j])
                    maxValueOfJ = j
                else:
                    break
            outerList.append(innerList)

    return outerList


def SayCount(inputList):
    finalResult = ""
    for numberGroup in inputList:
        occurrences = len(numberGroup)
        value = numberGroup[0]
        finalResult += str(occurrences) + str(value)
    return finalResult


def CountAndSayHelper(inputString):
    asList = []
    for element in inputString:
        asList.append(element)
    resultList = split(asList)
    return SayCount(resultList)


def CountAndSay(valueOfN):
    startingInput = "1"

    if valueOfN == 1:
        return "1"

    for n in range(1, valueOfN):
        startingInput = str(CountAndSayHelper(startingInput))

    return str(startingInput)


class TestSplit(TestCase):

    def test_empty_list(self):
        inputList = []
        self.assertEqual(first=[], second=split(inputList))

    def test_singleElement(self):
        inputList = [99]
        self.assertEqual(first=[[99]], second=split(inputList))

    def test_singleDuplicates(self):
        inputList = [1, 1]
        self.assertEqual(first=[[1, 1]], second=split(inputList))

    def test_twoDifferent_values(self):
        inputList = [2, 1]
        self.assertEqual(first=[[2], [1]], second=split(inputList))

    def test_second(self):
        inputList = [1, 2, 1, 1]
        self.assertEqual(first=[[1], [2], [1, 1]], second=split(inputList))

    def test_third(self):
        inputList = [1, 2, 1, 1, 1]
        self.assertEqual(first=[[1], [2], [1, 1, 1]], second=split(inputList))

    def test_fourth(self):
        inputList = [1, 2, 1, 1, 1, 4, 5, 5]
        self.assertEqual(first=[[1], [2], [1, 1, 1], [4], [5, 5]], second=split(inputList))


class TestSayCount(TestCase):

    def test_threeListsWithDuplicates(self):
        newlist = [[1], [2], [1, 1]]
        self.assertEqual(first="111221", second=SayCount(newlist))

    def test_specialCase(self):
        newlist = [[2], [1]]
        self.assertEqual(first="1211", second=SayCount(newlist))

    def test_singleElement(self):
        newlist = [[99]]
        self.assertEqual(first="199", second=SayCount(newlist))

    def test_Empty(self):
        newList = []
        self.assertEqual(first="", second=SayCount(newList))


class TestCountAndSayHelper(TestCase):

    def test_threeListsWithDuplicates(self):
        inputString = "21"
        self.assertEqual(first="1211", second=CountAndSayHelper(inputString))


    def test_withDuplicates(self):
        inputString = "11"
        self.assertEqual(first="21", second=CountAndSayHelper(inputString))


    def test_threeLists(self):
        inputString = "1211"
        self.assertEqual(first="111221", second=CountAndSayHelper(inputString))


class TestCountAndSay(TestCase):

    def test_Empty(self):
        n = 1
        self.assertEqual(first="1", second=CountAndSay(n))

    def test_NIsTwo(self):
        n = 2
        self.assertEqual(first="11", second=CountAndSay(n))

    def test_NIsThree(self):
        n = 3
        self.assertEqual(first="21", second=CountAndSay(n))

    def test_NIsFour(self):
        n = 4
        self.assertEqual(first="1211", second=CountAndSay(n))


if __name__ == '__main__':
    unittest.main()



