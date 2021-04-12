integers = [2, 1, 9]


def plusOne(digits):
    newStrings = [str(integer) for integer in digits]
    formString = "".join(newStrings)
    theInteger = int(formString)
    theInteger += 1
    reset = list(map(int, str(theInteger)))
    return reset


test = plusOne(integers)
print(test)
