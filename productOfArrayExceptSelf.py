def productExceptSelf(nums):
    if not nums or len(nums) == 0:
        return []
    length = len(nums)
    res = [1] * length
    L = 1
    for i in range(length):
        res[i] = res[i] * L
        L *= nums[i]

    R = 1
    for i in range(length - 1, -1, -1):
        res[i] = res[i] * R
        R *= nums[i]
    return res

nums = [6, 2, 3, 5, 9, 4, 7]
print(productExceptSelf(nums))