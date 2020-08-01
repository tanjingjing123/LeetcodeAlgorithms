def minInsertions(s):
    dp = {}
    N = len(s)
    for i in range(N):
        dp[i], j = {}, i
        while j > -1:
            if s[j]==s[i] and j >= i -1:
                dp[i][j] = 0
            elif s[j] == s[i]:
                dp[i][j] = dp[i-1][j+1]
            elif j == i - 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j+1])
            j -= 1
    return dp[N-1][0]

s = "leetcode"
print(minInsertions(s))