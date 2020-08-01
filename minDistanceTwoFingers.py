from functools import lru_cache

def minDistance(word):
    word = [ord(c) - ord('A') for c in word]

    def distance(a, b):
        return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

    dp = [0] * 26
    total = 0
    for i, (c1, c2) in enumerate(zip(word, word[1:])):
        d = distance(c1, c2)
        total += d
        for j in range(26):
            dp[c1] = max(dp[c1], dp[j] + d - distance(j, c2))

    return total - max(dp)

word = "HELLOW"
print(minDistance(word))