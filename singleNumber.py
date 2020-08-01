
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

nums = [4,2,9,3,2,3,9]
print(singleNumber(nums))