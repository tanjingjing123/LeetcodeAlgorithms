def sumRanges(nums):
    res = []
    if not len(nums):
        return res
    l = len(nums)
    s = 0
    while s < l:
        e = s + 1
        while e < l and nums[e] - nums[e - 1] == 1:
            e += 1
        if s == e - 1:
            res.append(str(nums[s]))
        else:
            res.append(str(nums[s]) + "->" + str(nums[e-1]))
        s = e
    return res

nums = [0,2,3,4,6,8,9]
print(sumRanges(nums))