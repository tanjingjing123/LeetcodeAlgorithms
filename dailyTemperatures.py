
def dailyTemperatures(T):
    res = [0] * len(T)
    stack = []
    for i in range(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res







t = [89,62,70,58,47,47,46,76,100,70]
print(dailyTemperatures(t))