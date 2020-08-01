def coinChange(coins, amount):
    frontier = {amount}
    coins.sort(reverse=True)
    res = 0
    seen = set()
    while frontier:
        if 0 in frontier:
            return res
        nxt_lst = set()
        for cur_amount in frontier:
            for c in coins:
                nxt = cur_amount - c
                if nxt >= 0 and nxt not in seen:
                    nxt_lst.add(nxt)
                    seen.add(nxt)
        frontier = nxt_lst
        res += 1
    return -1

coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))