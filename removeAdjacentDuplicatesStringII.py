def removeDuplicates(s, k):
    stack = []
    for i, ch in enumerate(s):
        if not stack or stack[-1][0] != ch:
            stack.append((ch, 1))
        else:
            val, count = stack.pop()
            if count + 1 != k:
                stack.append((val, count + 1))
    res = []
    for ch, count in stack:
        res += [ch] * count
    return "".join(res)

s = "pbbcggtttgciiicppooooapaais"
k = 3
print(removeDuplicates(s, k))
