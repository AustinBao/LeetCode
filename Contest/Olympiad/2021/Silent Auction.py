def silentAuction(numofbids, nameandpricelist):
    prices = []
    names = []
    for i in range(0, len(nameandpricelist) - numofbids):
        prices.append(nameandpricelist[(i*2) + 1])
        names.append(nameandpricelist[i*2])

    curr_max = 0
    for index, value in enumerate(prices):
        if curr_max < value:
            curr_max = value
            person = names[index]
    return person


print(silentAuction(6, ["Austin", 900, "Jerry", 900 ,"Ahmed", 300, "Suzanne", 500, "Ivona", 600, "Jordan", 600]))
