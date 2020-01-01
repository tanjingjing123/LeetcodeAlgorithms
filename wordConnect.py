def wrapLines(words, maxlength):
    res = []
    p = 0
    curStr = ""
    while p < len(words):
        if len(curStr) == 0:
            curStr += words[p]
            p += 1
        elif len(curStr) + 1 + len(words[p]) <= maxlength:
            curStr += "-"
            curStr += words[p]
            p += 1
        else:
            res.append(curStr)
            curStr = ""

    if len(curStr) != 0:
        res.append(curStr)
    return res


words = ["1p3acres", "is", "a", "good", "place", "to", "communicate"]
maxlength = 12
print(wrapLines(words, maxlength))