def wordBreak(s, words):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for end in range(1, len(s) + 1):
        for start in range(end):
            if dp[start] and s[start:end] in wordDict:
                dp[end] = True
                break
    return dp[-1]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))