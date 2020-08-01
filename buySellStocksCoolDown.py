def maxProfit(prices):
    if len(prices) < 1:
        return 0
    dp = [0] * len(prices)
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                dp[j] = dp[j-1]
                break
            dp[j] = max(dp[j], prices[j] - prices[i] + (dp[i-2] if (i-2)>=0 else 0), dp[j-1])
    return dp[-1]


prices = [9, 5, 7, 4, 2, 4, 1, 6, 4]
print(maxProfit(prices))