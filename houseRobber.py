def rob(nums):
    if not nums:
        return 0
    if len(nums)< 2:
        return max(nums)

    dp1 = [0, nums[0]]
    dp2 = [0, nums[1]]

    for idx in range(1, len(nums) - 1):
        dp1[0], dp1[1] = dp1[1], max(dp1[1], dp1[0] + nums[idx])

    for idx in range(2, len(nums)):
        dp2[0], dp2[1] = dp2[1], max(dp2[1], dp2[0] + nums[idx])

    return max(dp1[1], dp2[1])


nums = [4,2,5,7,1,2,3,2]
print(rob(nums))