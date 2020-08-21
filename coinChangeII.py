def change(amount, coins):
    dp = [1] + [0] * amount
    for c in coins:
        for i in range(1, amount + 1):
            if i - c >= 0:
                dp[i] += dp[i-c]
    return dp[-1]


amount = 5
coins = [1, 2, 5]
print(change(amount, coins))