def possibleChanges(usernames):
    compare = {}
    num = 1
    for letter in ("abcdefghijklmnopqrstuvwxyz"):
        compare[letter] = num
        num += 1

    decoded_name = []
    sublist = []
    for names in usernames:
        len_of_name = len(names)
        sublist.append(len_of_name)
        for let in names:
            decoded_name.append(compare[let])
    print(decoded_name)
    print(sublist)

    acc = []
    previous = 0
    after = 0
    for i in sublist:
        after += i
        acc.append(decoded_name[previous:after])
        previous += i

    solution = []
    end = -1
    for names in acc:
        for start in names:
            if names[end] < start:
                solution.append("YES")
                break
            else:
                solution.append("NO")
                break

    return solution