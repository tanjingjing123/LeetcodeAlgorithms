def numDecoding(s):
    if len(s) == 0:
        return 0

    dp = [0 for _ in range(len(s))]
    dp[-1] = 1 if s[-1] != '0' else 0

    for i in range(len(s) - 2, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            if s[i:i+2] <= '26':
                dp[i] = dp[i+1] + (dp[i+2] if i+2 < len(s) else 1)
            else:
                dp[i] = dp[i+1]
    return dp[0]
s = "102213421"
print(numDecoding(s))