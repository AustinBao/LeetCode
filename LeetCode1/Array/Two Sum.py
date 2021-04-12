lista = [2, 5, 7]


def twoSum(nums, target):
    # sorts out my list
    for k in range(0, len(nums)):
        for j in range(k + 1, len(nums)):
            if nums[k] > nums[j]:
                nums[k], nums[j] = nums[j], nums[k]


    for i in range(len(nums)):
        newtarget = target - nums[i]
        x = binarySearch(newtarget, nums)
        if x != "none":
            return [i,x]


def binarySearch(newtarget, nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == newtarget:
            return mid
        else:
            if newtarget < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return "none"


test = twoSum(lista, 7)
print(test)
