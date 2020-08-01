def checkRecord(n):
    if n == 1:
        return 3
    if n == 2:
        return 8
    mod = 10**9 + 7
    dp = [1, 2, 4, 7]
    current = 3
    while current < n:
        dp.append((dp[-1]*2-dp[-4]) % mod)
        current += 1
    ans = dp[-1]
    for i in range(n):
        ans = (ans + dp[n-i-1]*dp[i]) % mod
    return ans
