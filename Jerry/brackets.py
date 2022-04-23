def brackets(brackets_list):
    if len(brackets_list) == 0:
        return True
    openingBracket = brackets_list[0]
    nextBracket = brackets_list[1]
    if openingBracket == "(":
        rightClosing = ")"
        wrongClosing = "}"
    else:
        rightClosing = "}"
        wrongClosing = ")"
    if nextBracket == rightClosing:
        return brackets(brackets_list[2:])
    if nextBracket == wrongClosing:
        return False
    else:  # indicates the next bracket is an openingBracket
        if nextBracket == "(":
            closingToLookUpTo = ")"
        else:
            closingToLookUpTo = "}"
        if closingToLookUpTo in brackets_list:
            indices = [i for i, x in enumerate(brackets_list) if x == closingToLookUpTo]
            examineUpTo = first_even(indices)
            subListToExamine = brackets_list[1:examineUpTo + 1]
            listWithoutSublist = [openingBracket] + brackets_list[examineUpTo + 1:]
            return brackets(subListToExamine) and brackets(listWithoutSublist)
        return False


def first_even(x):
    for i in x:
        if i % 2 == 0:
            return i
    else:
        return x[0]


def split(word):
    return [char for char in word]


if __name__ == '__main__':
    print(brackets(split("({}{)}")))
    print(brackets(split("()")))
    print(brackets(split("(){}")))
    print(brackets(split("({){")))
    print(brackets(split("{{}}")))
    print(brackets(split("{()}")))
    print(brackets(split("{{}}()")))
    print(brackets(split("{(){{}}}()")))
