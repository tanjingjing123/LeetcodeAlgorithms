def maxSubarray(nums):
    max_cur, max_global = nums[0], nums[0]
    for i in range(1, len(nums)):
        max_cur = max(nums[i], nums[i] + max_cur)
        if max_cur > max_global:
            max_global = max_cur
    return max_global

nums  = [-13, -3, 15, -10, 3, 6, -3, -2, 5, 4, -7]
print(maxSubarray(nums))