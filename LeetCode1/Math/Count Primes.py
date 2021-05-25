def primecounter(n):
    containerlist = []
    if n == 0:
        return 0

    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            containerlist.append(i)
    return len(containerlist)


print(primecounter(10))
