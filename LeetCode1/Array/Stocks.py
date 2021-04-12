alist = [1, 2, 3, 4, 5]


def stonks(pricelists):
    ans = 0
    mini = pricelists[0]
    for i in range(1, len(pricelists)):
        if pricelists[i] < mini:
            mini = pricelists[i]
        else:
            ans = max(ans, pricelists[i] - mini)
    return ans


test = stonks(alist)
print(test)
