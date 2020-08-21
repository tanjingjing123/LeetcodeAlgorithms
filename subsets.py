
def subsets(nums):
    res = [[]]
    for i in range(len(nums)):
        res += [seq + [nums[i]] for seq in res]
    return res

nums = [1,2,3,4]
print(subsets(nums))

