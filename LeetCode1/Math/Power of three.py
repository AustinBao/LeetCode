
def cubedchecker(num):
    if num == 0:
        return False
    while num % 3 == 0:
        num /= 3
    return num == 1


print(cubedchecker(27))
print(cubedchecker(0))
print(cubedchecker(9))
print(cubedchecker(45))
print(cubedchecker(81))
