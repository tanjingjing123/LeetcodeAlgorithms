def longestCommonContinuousHistory(user1, user2):
    if not user1 or not user2:
        return []

    n1 = len(user1)
    n2 = len(user2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if user1[i-1] == user2[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]
    return dp[n1][n2]


user1 = ['3234.html', 'xys.html', '7hsaa.html']
user2 = ['3234.html', 'sdhsfjdsg.html', 'xys.html', '7hsaa.html']
print(longestCommonContinuousHistory(user1, user2))