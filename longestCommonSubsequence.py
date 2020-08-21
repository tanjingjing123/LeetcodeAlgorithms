def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)

    t = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j - 1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])
    return t[m][n]


text1 = "abcde"
text2 = "agcfefd"
print(longestCommonSubsequence(text1, text2))