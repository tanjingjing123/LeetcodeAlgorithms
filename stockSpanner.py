class StockSpanner:
    def __init__(self):
        self.prices = []


    def next(self, price):
        weight = 1
        while self.prices and self.prices[-1][0] <= price:
            weight += self.prices.pop()[1]
        self.prices.append((price, weight))
        return weight

S = StockSpanner()
print(S.next(28))
print(S.next(14))
print(S.next(28))
print(S.next(35))
print(S.next(46))
print(S.next(53))
print(S.next(66))
print(S.next(80))
print(S.next(87))
print(S.next(88))


# [[],[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]



