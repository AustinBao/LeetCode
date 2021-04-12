alist = [1, 7, 3, 4, 5]


def stonks(pricelists):
    ans = 0
    for i in range(1, len(pricelists)):
        if pricelists[i-1] < pricelists[i]:
            ans += pricelists[i] - pricelists[i-1]
    return ans

test = stonks(alist)
print(test)
