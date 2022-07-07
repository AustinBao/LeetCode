def sameparking(n, day1, day2):
    similar = 0
    for i in range(0, n):
        if day1[i] == "C" and day2[i] == "C":
            similar += 1
        else: # no need for this else statement
            continue
    return similar


print(sameparking(5, ["C", "C", ".", ".", "C"], [".", "C", ".", ".", "."]))
print(sameparking(5, ["C", "C", "C", "C", "C"], [".", "C", "C", "C", "C"]))

