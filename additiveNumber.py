def isadditive(num):
    def additive(S, ind, ans):
        if ind == len(S) and len(ans) > 2:
            return True
        res = False
        for i in range(ind, len(S)):
            p = S[ind:i+1]
            if len(p) > 1 and p[0] == "0":
                continue
            if len(ans) >= 2 and int(ans[-2]) + int(ans[-1]) != int(p):
                continue
            ans.append(p)
            res = res or additive(S, i+1, ans)
            ans.pop()
        return res
    return additive(num, 0, [])

num = "199100199"
print(isadditive(num))