
def subsets(nums):
    res = []
    for num in range(2**len(nums)):
        idx = 0
        combine = []
        while num:
            if num & 1:
                combine.append(nums[idx])
            idx += 1
            num >>= 1
        else:
            res.append(combine)
    return res

nums = [1,2,3,4]
print(subsets(nums))

