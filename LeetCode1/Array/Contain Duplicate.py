myList = [1, 2, 3, 3]


def containDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    for k in range(0, len(nums)):
        for m in range(k + 1, len(nums)):
            if nums[k] == nums[m]:
                return True

    return False

# Looks good,
# A better, more efficient implementation is possible using a sorting algorithm (ignore that for now)
# Try to create an algorithm that only uses one nested for loop, hint: you wont need to sort it.

User1 = containDuplicate(myList)
print(User1)
