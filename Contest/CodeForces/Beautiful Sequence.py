tc = int(input())
for i in range(tc):
    sd = input()
    n = list(input())

    for i in n:
        if i == " ":
            n.remove(i)


    def allSubsequences(l):
        if len(l) == 0:
            return [[]]
        x = allSubsequences(l[1:])
        return x + [[l[0]] + y for y in x]


    list_of_lists = allSubsequences(n)


    def checksubsequence(lol):
        for l in lol:
            for num in range(1, len(l) + 1):
                if str(num) == l[num - 1]:
                    return "YES"
        return "NO"


    print(checksubsequence(list_of_lists))
