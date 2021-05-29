myList = [2, 3, 4, 1, 2]


def containDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# Looks good,
# A better, more efficient implementation is possible using a sorting algorithm (ignore that for now)
# Try to create an algorithm that only uses one nested for loop, hint: you wont need to sort it.

User1 = containDuplicate(myList)
print(User1)
