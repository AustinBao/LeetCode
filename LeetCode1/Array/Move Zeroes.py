lista = [0, 1, 0, 3, 2, 4, 0, 7, 0, 0]


def moveZeroes(nums):
    for k in range(0, len(nums)):
        for j in range(k + 1, len(nums)):
            if nums[k] == 0:
                nums[k], nums[j] = nums[j], nums[k]
    return nums


test = moveZeroes(lista)
print(test)
