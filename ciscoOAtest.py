line = "(abb(cd){3}){3}"
strstack = []
curStr = ""
for i, c in enumerate(line):
    if c == "(":
        strstack.append(curStr[::])
        curStr = ""
    elif c == ")":
        strstack.append(curStr[::])
        curStr = ""
    elif c == "{":
        curStr = ""
    elif c == "}":
        times = int(curStr)
        curStr = strstack.pop()
        curStr *= times
        curStr = strstack.pop() + curStr
    else:
        curStr += c


while strstack:
    curStr = strstack.pop() + curStr

print(curStr)