s = "masck"
t = "maskc"

def anagramvalid(str1, str2):
    dictionary = {}
    dictionary2 = {}

    for i in str1:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    for i in str2:
        if i not in dictionary2:
            dictionary2[i] = 1
        else:
            dictionary2[i] += 1
    if dictionary == dictionary2:
        return True
    return False

test = anagramvalid(s,t)
print(test)