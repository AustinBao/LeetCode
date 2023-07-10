first = input()
second = input()


def Letters(word):
    letters = {}
    for i in word:
        if i == " ":
            continue
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters


for i in Letters(first):
    if i not in Letters(second):
        print("Is not an anagram")
        break
    elif Letters(first)[i] != Letters(second)[i]:
        print("Is not an anagram")
        break
    print("Is an anagram")
    break
