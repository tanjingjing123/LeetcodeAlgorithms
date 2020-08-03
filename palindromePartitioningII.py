def minCut(s):
    memo = [[] for i in range(len(s))]  # To store length of palindromes starting at index i
    for i in range(len(s)):
        a = i
        b = i
        while a >= 0 and b < len(s) and s[a] == s[b]:
            memo[a].append(b - a + 1)
            a -= 1
            b += 1
        a = i
        b = i + 1
        while a >= 0 and b < len(s) and s[a] == s[b]:
            memo[a].append(b - a + 1)
            a -= 1
            b += 1

    dp = [float("inf")] * (len(s) + 1)
    dp[len(s)] = -1
    for i in range(len(s) - 1, -1, -1):
        for j in memo[i]:
            dp[i] = min(dp[i], 1 + dp[i + j])
    return dp[0]

s = "aababbabb"
print(minCut(s))