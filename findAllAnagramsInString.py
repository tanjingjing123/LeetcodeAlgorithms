def findAnagrams(s, p):
    m, n = len(p), len(s)
    def hash(c):
        return 31**(c-96)
    d = {chr(c): hash(c) for c in range(ord('a'), ord('z')+1)}

    pc = sum(d[c] for c in p)
    window = sum(d[c] for c in s[:m])
    ans = []
    for i in range(m, n):
        if window == pc:
            ans.append(i-m)
        window = window - d[s[i-m]] + d[s[i]]

    if window == pc:
        ans.append(n-m)
    return ans

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
