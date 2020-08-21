def calculate(s):
    integers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    operators = {"+", "-", "*", "/", "(", ")"}

    s = s.replace(" ", "")
    l = []
    for idx in range(len(s)):
        if s[idx] in operators:
            l.append(s[idx])
        if s[idx] in integers and (idx == len(s) - 1 or s[idx + 1] in operators):
            start = idx
            while start > 0 and s[start - 1] in integers:
                start -= 1
            l.append(int(s[start:idx + 1]))

    stack = []
    def operate(value):
        if not stack:
            stack.append(value)
        else:
            if stack[-1] == '*':
                stack.pop()
                num = stack.pop()
                stack.append(num * value)
            elif stack[-1] == '/':
                stack.pop()
                num = stack.pop()
                stack.append(int(num/value))
            elif stack[-1] == '-':
                stack.pop()
                stack.append(-value)
            else:
                stack.append(value)

    for elem in l:
        if elem in {"-", "*", "/"}:
            stack.append(elem)
        elif elem == "(":
            stack.append(elem)
        elif elem == ")":
            tmp = 0
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()
            operate(tmp)
        elif isinstance(elem, int):
            operate(elem)
    return sum(stack)


s = "(1+(4+501+2)-32)+(16+8)"
print(calculate(s))
