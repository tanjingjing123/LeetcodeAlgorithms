def maxSubarray(nums):
    max_cur = nums[0]
    max_global = nums[0]
    for i in range(1, len(nums)):
        max_cur = max(nums[i], nums[i] + max_cur)
        if max_cur > max_global:
            max_global = max_cur
    return max_global

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarray(nums))