nums = [1, 2, 3, 4, 5]
moveright = 6
storage = []


def rotate(inputlist, rotate):
    i = 0
<<<<<<< HEAD
=======
    j = -1
    # Looks good, but the code can be made shorter, do you see any duplicate code?
>>>>>>> b2082ddd913661efb22a91d4d55b7ffe15d45b9c
    if rotate > len(inputlist):
        y = rotate % len(inputlist)
    else:
        y = rotate

    while i != y:
        x = inputlist.pop(-1)
        storage.append(x)
        i += 1

    storage.reverse()
    storage.extend(inputlist)

    return storage


test = rotate(nums, moveright)
print(test)
