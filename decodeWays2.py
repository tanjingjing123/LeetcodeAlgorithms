def numDecodings(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0

    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(n):
        if s[i] == '*':
            dp[i+1] += dp[i] * 9
            if i>0:
                if s[i-1] == '1':
                    dp[i+1] += dp[i-1] * 9
                elif s[i-1] == '2':
                    dp[i+1] += dp[i-1] * 6
                elif s[i-1] == '*':
                    dp[i+1] += dp[i-1] * 15
        else:
            if '1' <= s[i] <= '9':
                dp[i+1] += dp[i]
            if i>0:
                if '10' <= s[i-1:i+1] <= '26':
                    dp[i+1] += dp[i-1]
                elif '*0' <= s[i-1:i+1] <= '*6':
                    dp[i+1] += 2 * dp[i-1]
                elif '*7' <= s[i-1:i+1] <= '*9':
                    dp[i+1] += dp[i-1]
        dp[i+1] %= (10 ** 9 + 7)
    return dp[n]

s = "1*20"
print(numDecodings(s))