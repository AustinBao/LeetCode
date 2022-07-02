def palindrome(word):
    pal = []
    for iteration in range(0, len(word)):
        temp = []
        for i in word:
            temp.append(i)
        pal.append(temp)

    for index1, words in enumerate(pal):
        for index2, letters in enumerate(words):
            words.pop(index1)
            if words == words[::-1]:
                return index1
            break

    return -1


print(palindrome(""))

print(palindrome("nbna"))

print(palindrome("nbnaa"))
