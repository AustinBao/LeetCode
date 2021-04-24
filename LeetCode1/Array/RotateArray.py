nums = [1,2,3,4,5]
moveright = 6
storage = []

def rotate(inputlist, rotate):
    i = 0
    j = -1
    # Looks good, but the code can be made shorter, do you see any duplicate code?
    if rotate > len(inputlist):
        y = rotate % len(inputlist)
        while i != y:
            x = inputlist.pop(j)
            storage.append(x)
            i += 1
        storage.reverse()
    else:
        while i != rotate:
            x = inputlist.pop(j)
            storage.append(x)
            i += 1
        storage.reverse()

    storage.extend(inputlist)

    return storage

test = rotate(nums, moveright)
print(test)
