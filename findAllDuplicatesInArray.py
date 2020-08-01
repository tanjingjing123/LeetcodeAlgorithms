def findDuplicates(nums):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == i + 1:
            i += 1
        elif nums[i] == nums[nums[i]-1]:
            i += 1
        else:
            a, b = i, nums[i]-1
            nums[a], nums[b] = nums[b], nums[a]

    res = []
    for i in range(n):
        if i + 1 != nums[i]:
            res.append(nums[i])
    return res

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))