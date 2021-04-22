number = 6573290


def reverse(num):
    k = []
    j = -1
    newstr = ""
    version = list(str(num))

    for i in version:
        k.append(version[j])
        j -= 1

    for ele in k:
        if ele != 0:
            newstr += ele

    return int(newstr)


User1 = reverse(number)
print(User1)
