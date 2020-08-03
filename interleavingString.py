def isInterleave(a, b, c):
    if len(a) + len(b) != len(c): return False

    def f(a, b, c, i, j, d):
        k = i + j
        l1, l2, l3 = len(a), len(b), len(c)
        if i == l1 and j == l2: return True
        if (i, j) in d: return d[i, j]
        ans = False
        if i < l1 and a[i] == c[k]: ans = f(a, b, c, i + 1, j, d) or ans
        if j < l2 and b[j] == c[k]: ans = f(a, b, c, i, j + 1, d) or ans
        d[i, j] = ans
        return ans
    return f(a, b, c, 0, 0, {})

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1,s2,s3))