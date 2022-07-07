def shifts(word, string):

    cycles = [string]
    for i in range(1, len(string)):
        newstr = ""
        newstr += string[i:]
        newstr += string[:i]
        cycles.append(newstr)

    for words in cycles:
        if words in word:
            return "Yes"
    return "No"


print(shifts("CDEABFGHIJKLM", "ABCDE"))

print(shifts("ABCDDEBCAB", "ABA"))

