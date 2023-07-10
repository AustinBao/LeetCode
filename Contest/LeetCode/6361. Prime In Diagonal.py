def diagonalPrime(nums):
    if len(nums) == 0:
        return 0

    otherdiagonal = nums[::-1]
    largestprime = 0

    for i in range(len(nums)):
        if nums[i][i] > otherdiagonal[i][i]:
            if largestprime < otherdiagonal[i][i] and isprime(otherdiagonal[i][i]) is True:
                largestprime = otherdiagonal[i][i]
            if largestprime < nums[i][i] and isprime(nums[i][i]) is True:
                largestprime = nums[i][i]
        else:
            if largestprime < nums[i][i] and isprime(nums[i][i]) is True:
                largestprime = nums[i][i]
            if largestprime < otherdiagonal[i][i] and isprime(otherdiagonal[i][i]) is True:
                largestprime = otherdiagonal[i][i]

    return largestprime


def isprime(integer):
    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True


print(diagonalPrime([[1, 2, 3], [5, 15, 7], [9, 11, 10]]))

print(diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))

print(diagonalPrime([[885, 547, 520, 806], [690, 260, 449, 529], [435, 635, 311, 714], [143, 302, 549, 412]]))
