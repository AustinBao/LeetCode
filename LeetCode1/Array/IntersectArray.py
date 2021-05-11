list1 = [1, 3, 2, 1]
list2 = [1, 3]


def intersect(nums1, nums2):
    i = 0
    j = 0
    result = []
    nums1.sort()
    nums2.sort()

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result


test1 = intersect(list1, list2)
print(test1)
