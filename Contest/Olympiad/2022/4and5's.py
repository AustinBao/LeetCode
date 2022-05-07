def sumOfFourAndFives(num):
    num_of_sums = 0
    max_fours = num // 4
    trials_of_four = list(range(0, max_fours + 1))
    list_remainder = []
    for number in trials_of_four:
        x = (num - (number * 4)) % 5
        if x == 0:
            num_of_sums += 1
        list_remainder.append(x)

    return num_of_sums, list_remainder


print(sumOfFourAndFives(50))
print(sumOfFourAndFives(100))
print(sumOfFourAndFives(200))
print(sumOfFourAndFives(300))
print(sumOfFourAndFives(9000))
