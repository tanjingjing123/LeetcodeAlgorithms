def countNumUniqueDigits(n):
    if n in (0, 1):
        return 1 if n == 0 else 10
    res = [1, 10]
    c = 9
    while n > 1:
        res.append((res[-1]-res[-2])*c + res[-1])
        n -= 1
        c -= 1

    return res[-1]

print(countNumUniqueDigits(4))