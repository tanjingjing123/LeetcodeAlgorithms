
def minRemove(s):
    ret = list(s)
    stack = []
    index_to_remove = []

    for i, c in enumerate(ret):
        if c == '(':
            stack.append(c)
            index_to_remove.append(i)

        elif c == ')':
            if not stack:
                ret[i] = ""
            else:
                stack.pop()

    if stack:
        for i in index_to_remove[-len(stack):]:
            ret[i] = ""

    return "".join(ret)

s = "lee(t(c)o)d)e)e(("
print(minRemove(s))