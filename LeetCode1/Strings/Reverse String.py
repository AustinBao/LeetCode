input = ["w","o","h"]
extra = []

def reverse(word):
    i = -1
    for k in word:
        extra.append(word[i])
        i-=1

    return extra

User1 = reverse(input)
print(User1)