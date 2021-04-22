s = "crack"
t = "racck"


def anagramvalid(str1, str2):
    dictionary = {}
    for i in range(len(str1)):
        if str1[i] not in dictionary:
            dictionary[str1[i]] = 1
        else:
            dictionary[str1[i]] + 1

    return dictionary


test = anagramvalid(s, t)
print(test)
