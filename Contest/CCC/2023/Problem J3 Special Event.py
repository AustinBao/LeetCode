number_of_people = int(input())
best_days = []
count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for people in range(number_of_people):
    schedule = input()
    for day in range(len(schedule)):
        if schedule[day] == "Y":
            count[day + 1] += 1

maximum = 0
for key in count:
    if count[key] > maximum:
        maximum = count[key]

for key in count:
    if count[key] == maximum:
        best_days.append(str(key))

print(",".join(best_days))

# import unittest
# from unittest import TestCase
#
#
# def SpecialEvent(number_of_people, days_available):
#     if number_of_people == 0:
#         return
#
#     best_days = []
#     count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
#
#     for schedule in days_available:
#         for day in range(len(schedule)):
#             if schedule[day] == "Y":
#                 count[day] += 1
#
#     maximum = 0
#     for key in count:
#         if count[key] > maximum:
#             maximum = count[key]
#
#     for key in count:
#         if count[key] == maximum:
#             best_days.append(str(key))
#
#     return ", ".join(best_days)
#
#
# class TestSpecialEvents(TestCase):
#
#     def test_one_day(self):
#         number_of_people = 3
#         days_available = ["YY.Y.",
#                           "...Y.",
#                           ".YYY."]
#         self.assertEqual(first="3", second=SpecialEvent(number_of_people, days_available))
#
#     def test_more_than_one_day(self):
#         number_of_people = 3
#         days_available = ["YY.Y.",
#                           ".Y.Y.",
#                           ".YYY."]
#         self.assertEqual(first="1, 3", second=SpecialEvent(number_of_people, days_available))
#
#     def test_zero_people(self):
#         number_of_people = 0
#         days_available = []
#         self.assertEqual(first=None, second=SpecialEvent(number_of_people, days_available))
#
#     def test_sample_input_2(self):
#         number_of_people = 5
#         days_available = ["YY..Y",
#                           ".YY.Y",
#                           ".Y.Y.",
#                           ".YY.Y",
#                           "Y...Y"]
#         self.assertEqual(first="1, 4", second=SpecialEvent(number_of_people, days_available))
#
#
# if __name__ == '__main__':
#     unittest.main()
