def isValid(s):
    if not s:
        return True
    stack = []

    if len(s) == 1:
        return False

    for c in s:
        if c in ("(", "[", "{"):
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                top = stack.pop()
                if c == ")" and top == '(':
                    continue
                elif c == ']' and top == '[':
                    continue
                elif c == '}' and top == '{':
                    continue
                else:
                    return False
    return True if not stack else False

s = "[])"
print(isValid(s))