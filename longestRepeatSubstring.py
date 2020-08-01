def longestSubstring(S):
    substrings = dict()
    maxLen = 0
    for k in range(1, len(S)):
        flag = False
        for i in range(len(S)):
            j = i + k
            if j > len(S):
                break

            if S[i:j] in substrings:
                maxLen = max(maxLen, k)
                flag = True
                break
            else:
                substrings[S[i:j]] = 1
        if not flag:
            break

    return maxLen

S = "aabcaabdaab"
print(longestSubstring(S))