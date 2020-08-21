
def maxProfit(prices):
    maxProfit = 0
    minPrice = prices[0]
    for price in prices[1:]:
        if price >= minPrice:
            maxProfit = max(maxProfit, price - minPrice)
        else:
            minPrice = min(minPrice, price)
    return maxProfit

prices = [7, 6, 1, 5, 3, 6, 4]
print(maxProfit(prices))