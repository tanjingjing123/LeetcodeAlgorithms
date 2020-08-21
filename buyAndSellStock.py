import collections
import heapq
def maxProfit(stocks, M):
    h = []
    counts = {}
    for x in stocks:
        rate = float((x[1] - x[0])/x[0])
        counts[x[0]] = x[2]
        h.append((-rate, x[0], x[1]))
    heapq.heapify(h)

    revenue = 0
    remain = M
    while h and remain > 0:
        rate, buy, sell = heapq.heappop(h)
        while counts[buy] > 0 and remain > buy:
            revenue += sell
            counts[buy] -= 1
            remain -= buy

        if counts[buy] == 0:
            continue

        if counts[buy] > 0 and remain > 0 and remain <= buy:
            units = float(remain/buy)
            revenue += units * sell
            remain -= units * buy

    return revenue

stocks = [[30, 55, 3], [35, 50, 3], [20, 30, 2], [40, 60, 3], [50, 80, 2]]
M = 250
print(maxProfit(stocks, M))


