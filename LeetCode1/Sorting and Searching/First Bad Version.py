import unittest
from unittest import TestCase


def badVersionFinder(number_of_ver, bad_ver):
    list_of_versions = list(range(1, number_of_ver + 1))
    print(list_of_versions)

    for num_in_list in list_of_versions:
        if num_in_list == bad_ver:
            print(num_in_list, "is the bad version")

            while num_in_list != len(list_of_versions):
                num_in_list += 1
                print(num_in_list, "is the bad version")
            return
        else:
            print(num_in_list, "is good")


def badVersionFinderB(number_of_ver, bad_ver):
    list_of_versions = list(range(1, number_of_ver + 1))
    for version in list_of_versions:
        if version >= bad_ver:
            print(version, "is bad")
        else:
            print(version, "is good")


badVersionFinderB(5,2)


def isVersionBad(bad_version, version_to_check):
    return bool(bad_version <= version_to_check)

print(isVersionBad(4, 1))


class TestisVersionBad(TestCase):

    def test_equal(self):
        self.assertEqual(first=True, second=isVersionBad(1,1))

    def test_badVersionGreater(self):
        self.assertEqual(first=False, second=isVersionBad(3,1))

    def test_badVersionLesser(self):
        self.assertEqual(first=True, second=isVersionBad(1,3))


if __name__ == '__main__':
    unittest.main()