from collections import Counter
def characterReplace(s, k):
    start = maxCnt = res = 0
    counts = Counter()
    for i, char in enumerate(s):
        counts[char] += 1
        maxCnt = max(maxCnt, counts[char])
        if (i - start + 1) - maxCnt > k:
            counts[s[start]] -= 1
            start += 1
        res = max(res, i - start + 1)
    return res


s = "AABADBCBA"
k = 2
print(characterReplace(s, k))