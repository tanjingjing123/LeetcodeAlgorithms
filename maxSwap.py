def maxswap(num):
    n = str(num)
    maxCarry = [[int(n[-1]), len(n) - 1]]
    for i in range(len(n) - 2, -1, -1):
        if int(n[i]) > maxCarry[-1][0]:
            maxCarry.append([int(n[i]), i])
        else:
            maxCarry.append(maxCarry[-1])

    for i in range(len(n)):
        if int(n[i]) < maxCarry[-(i+1)][0]:
            j = maxCarry[-(i+1)][1]
            res = n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:]
            return int(res)

    return int(n)



num = 25723865
print(maxswap(num))