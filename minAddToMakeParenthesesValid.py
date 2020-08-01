def minAddToMakeValid(S):
    l, r = 0, 0
    for i in S:
        if i == '(':
            l += 1
        elif i == ')':
            if l == 0:
                r += 1
            elif l != 0:
                l -= 1
    return (l + r)

S = "())))())(((("
print(minAddToMakeValid(S))