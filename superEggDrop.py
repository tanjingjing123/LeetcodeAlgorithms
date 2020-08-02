def superEggDrop(K, N):
    def dfs(k, n):
        if k == 1:
            return n
        if n == 0:
            return 0
        if n == 1:
            return 1

        if (k, n) in memo:
            return memo[(k, n)]

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            x = dfs(k - 1, mid - 1)
            y = dfs(k, n - mid)
            if x < y:
                lo = mid + 1
            else:
                hi = mid
        res = 1 + max(dfs(k - 1, lo - 1), dfs(k, n - lo))
        memo[(k, n)] = res
        return res
    memo = {}
    return dfs(K, N)



print(superEggDrop(3, 14))