def toothpaste(tubes, n):
    whole_tubes = tubes
    extra_tubes = 0

    while whole_tubes >= n:
        whole_tubes -= n
        whole_tubes += 1
        extra_tubes += 1

    return extra_tubes + tubes


print(toothpaste(23, 4))
print(toothpaste(4, 2))
print(toothpaste(173, 90))

