def maxProfit(k, prices):
    if len(prices) <= 1:
        return 0

    if k >= len(prices) // 2:
        return sum([i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0])

    dp = [[0] * len(prices) for _ in range(k + 1)]
    for i in range(1, len(dp)):
        max_diff = -prices[0]
        for j in range(1, len(dp[i])):
            dp[i][j] = max(dp[i][j-1], max_diff + prices[j])
            max_diff = max(max_diff, dp[i-1][j] - prices[j])

    return dp[-1][-1]
prices = [3,2,6,5,0,3,7,10,3,2]
k = 3
print(maxProfit(k, prices))