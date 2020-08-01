def removeInvalidParentheses(s):
    l = 0
    r = 0
    for char in s:
        l += (char == '(')
        if l == 0:
            r += (char == ')')
        else:
            l -= (char == ')')

    def isValid(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def dfs(s, start, l, r, ans):
        if l == 0 and r == 0:
            if isValid(s):
                ans.append(s)
            return

        for i in range(start, len(s)):
            if i != start and s[i] == s[i-1]:
                continue
            if s[i] == '(' or s[i] == ')':
                ns = s[:i] + s[i+1:]
                if r > 0:
                    dfs(ns, i, l, r-1, ans)
                elif l > 0:
                    dfs(ns, i, l - 1, r, ans)

    ans = []
    dfs(s, 0, l, r, ans)
    return ans



s = "(a)())()"
print(removeInvalidParentheses(s))