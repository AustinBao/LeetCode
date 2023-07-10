numofcases = int(input())

opened = []
c = 0
while c != numofcases:
    c += 1
    opened.append(int(input()))

opened.sort()

cases = {
    1: 100,
    2: 500,
    3: 1000,
    4: 5000,
    5: 10000,
    6: 25000,
    7: 50000,
    8: 100000,
    9: 500000,
    10: 1000000,
}

removed = 0
for num in opened:
    removed += cases[num]

total = 1691600 - removed
offer = int(input())


if total / (10 - numofcases) > offer:
    print("no deal")
else:
    print("deal")
