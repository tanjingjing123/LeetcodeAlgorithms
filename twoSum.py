def twoSum(nums, target):
    subt = dict()
    for i in range(len(nums)):
        if nums[i] in subt:
            return [i, subt[nums[i]]]
        else:
            subt[target - nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))