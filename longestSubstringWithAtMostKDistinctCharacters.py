import collections
def lengthSubstring(s, k):
    def trimAndUpdate(left, right):
        while left <= right:
            dic[s[left]] -= 1
            if dic[s[left]] == 0:
                left += 1
                break
            left += 1
        return left

    left, right = 0, 0
    dic = collections.defaultdict(int)
    totalDistinct = 0
    maxLen = 0
    while right < len(s):
        if dic[s[right]] == 0:
            totalDistinct += 1
        dic[s[right]] += 1

        if totalDistinct == k + 1:
            left = trimAndUpdate(left, right)
            totalDistinct -= 1
        maxLen = max(maxLen, right - left + 1)
        right += 1
    return max(maxLen, right - left)

s = "ecebaaqa"
k = 2
print(lengthSubstring(s, k))