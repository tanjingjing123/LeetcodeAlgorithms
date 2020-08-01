import math


def splitArray(nums, m):
    if not nums:
        return 0
    n = len(nums)
    dp = [[math.inf for j in range(m)] for i in range(n)]
    dp[0][0] = nums[0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + nums[i]
    for i in range(1, n):
        for j in range(1, m):
            for k in range(i):
                dp[i][j] = min(dp[i][j], max(dp[k][j-1], dp[i][0]-dp[k][0]))
    return dp[n-1][m-1]

nums = [7,2,5,10,8,4,6,3]
k = 4
print(splitArray(nums, k))