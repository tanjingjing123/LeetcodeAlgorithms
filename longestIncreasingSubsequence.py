class solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

obj = solution()
nums = [10,9,2,5,3,7,101,18]
print(obj.lengthOfLIS(nums))