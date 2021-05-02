s = "tacocat"


def palindromevalid(str1):
    new = []
    for i in str1:
        new.append(i)
    reversed = new[::-1]
    if reversed == new:
        return True
    return False


user = palindromevalid(s)
print(user)
