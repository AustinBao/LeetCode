new = [4, 2, 5]
node = 0


def nthnode(linked, nth):
    if nth > len(linked) - 1:
        linked.pop(-1)
        return linked
    else:
        linked.pop(nth)
    return linked


test = nthnode(new, node)
print(test)
