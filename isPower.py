import math
def isPower(nums):
    res = []
    for num in nums:
        if 2**int(math.log(num, 2)) == num:
            res.append(1)
        else:
            res.append(0)
    return res

nums = [1, 3, 8, 12, 16]
print(isPower(nums))
