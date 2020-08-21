def maxProfit(prices, fee):
    cash = 0
    hold = -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash

prices = [1, 3, 4, 2, 9, 5, 12]
fee = 3
print(maxProfit(prices, fee))