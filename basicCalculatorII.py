def calculate(s):
    stack = []
    now = ''
    operator = '+'
    s += '#'
    for ch in s:
        if ch == ' ':
            continue
        elif ch.isdigit():
            now += ch
            continue

        if operator == '+':
            stack.append(int(now))
        elif operator == '-':
            stack.append(-int(now))
        elif operator == '*':
            top = stack.pop()
            stack.append(int(top) * int(now))
        elif operator == '/':
            top = stack.pop()
            res = 0
            if int(top) < 0 and int(top) % int(now) != 0:
                res = int(top) // int(now) + 1
            else:
                res = int(top) // int(now)
            stack.append(res)

        now = ''
        operator = ch

    return sum(stack)
s = "3/2"
print(calculate(s))
