import collections
def firstMissingPositive(nums):
    if len(nums) == 0:
        return 1
    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i

nums = [7,6,-4,2,9,5,3,-7,8,-4,11,1,10,4]
print(firstMissingPositive(nums))