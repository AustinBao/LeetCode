def sumOfFourAndFives(num):
    num_of_sums = 0
    max_fours = num // 4
    trials_of_four = list(range(0, max_fours + 1))
    for number in trials_of_four:
        if (num - (number * 4)) % 5 == 0:
            num_of_sums += 1
    return num_of_sums


print(sumOfFourAndFives(7))

print(sumOfFourAndFives(80))



