def numRollsToTarget(d, f, target):
    if target > f * d or target < d:
        return 0

    dp = [[0] * (target + 1) for _ in range(d+1)]
    dp[0][0] = 1
    for i in range(1, d+1):
        for t in range(1, target + 1):
            dp[i][t] = sum(dp[i-1][t-j] for j in range(1, f+1) if t-j>=0)
    return dp[d][target] % (10**9+7)

print(numRollsToTarget(6, 7, 8))


