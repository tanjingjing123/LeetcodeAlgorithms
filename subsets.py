
def subsets(nums):
    res = [[]]
    for i in range(len(nums)):
        tmp = res[::]
        for seq in tmp:
            res.append(seq + [nums[i]])
    return res

nums = ['John', 'Amy', 'Vincent']
print(subsets(nums))

