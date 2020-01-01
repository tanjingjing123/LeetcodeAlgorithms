import collections

def findDupicates(nums):
    res = set()
    i = 0
    while i < len(nums):
        while i != nums[i] - 1:
            target = nums[i] - 1
            if nums[target] == nums[i]:
                res.add(nums[i])
                i += 1
            else:
                nums[i], nums[target] = nums[target], nums[i]
        i += 1
    return list(res)

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDupicates(nums))