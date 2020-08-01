def isMatch(s, p):
    dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
    dp[0][0] = True

    for i in range(1, len(dp)):
        if p[i-1] == '*':
            dp[i][0] = dp[i-1][0]


    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if p[i-1] == s[j-1] or p[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]

            if p[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

    return dp[-1][-1]


s = "adceb"
p = "*a*b"
print(isMatch(s, p))