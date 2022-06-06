def containDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def containDuplicate2(nums):
    dictionary = {}
    for elements in nums:
        if dictionary.get(elements) == 1:
            return True
        else:
            dictionary[elements] = 1
    return False


# Looks good,
# A better, more efficient implementation is possible using a sorting algorithm (ignore that for now)
# Try to create an algorithm that only uses one nested for loop, hint: you wont need to sort it.

# print(containDuplicate([2, 3, 4, 1, 2]))

print(containDuplicate2([3, 4, 1, 3, 2]))
print(containDuplicate2([0,0, 9]))

