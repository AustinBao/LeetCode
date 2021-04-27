myList = [2, 3, 4, 1, 2]


def containDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

User1 = containDuplicate(myList)
print(User1)
