def maxProfit(prices, fee):
    profit = 0
    state = -prices[0]
    for p in prices:
        profit = max(profit, state + p - fee)
        state = max(state, profit - p)
    return profit

prices = [1, 3, 4, 2, 9, 5, 12]
fee = 3
print(maxProfit(prices, fee))