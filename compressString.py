def compress(word, k):
    stack = []
    for c in word:
        if not stack:
            stack.append([c, 1])
        else:
            if c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

        while stack and stack[-1][1] >= k:
            stack.pop()

    res = ""
    for ele in stack:
        res += ele[0] * ele[1]
    return res


word = "addceeeccdaf"
k = 3
print(compress(word, k))