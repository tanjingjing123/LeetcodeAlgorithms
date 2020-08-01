def countSubstrings(s):
    snum = len(s)
    if snum == 0:
        return 0
    elif snum == 1:
        return 1
    else:
        ans = 0
        dp = [[0] * snum for _ in range(snum)]
        for j in range(snum):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        if j - i > 1:
                            dp[i][j] = 1 if dp[i+1][j-1] else 0
                        else:
                            dp[i][j] = 1
                if dp[i][j] == 1:
                    ans += 1
    return ans

s = "aababbccaba"
print(countSubstrings(s))
