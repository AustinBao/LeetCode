def kalendar(n, d):
    curr = "+---------------------+\n|"
    counter = 1

    if n <= 7:
        for i in range(1, 8):
            if i == d:
                for j in range(n):
                    curr += "..{}".format(counter)
                    counter += 1
                break
            curr += "..."

        if n == 1:
            curr += "..." * int(7-d)
        else:
            curr += "..." * int(7 - n)
        curr += "|\n"
        return curr

    for i in range(1, 8):
        if i == d:
            for j in range(8 - i):
                curr += "..{}".format(counter)
                counter += 1
            curr += "|\n"
            break
        curr += "..."

    while counter < n:
        curr += "|"
        for i in range(1, 8):
            if counter == n + 1:
                curr += "..."
                continue
            else:
                if counter >= 10:
                    curr += ".{}".format(counter)
                    counter += 1
                else:
                    curr += "..{}".format(counter)
                    counter += 1
        curr += "|\n"
    curr += "+---------------------+\n"
    return curr


print(kalendar(4, 1))
