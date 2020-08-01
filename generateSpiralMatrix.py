def generateMatrix(n):
    res = [[0] * n for _ in range(n)]
    up, down = 0, n - 1
    left = 0
    right = n - 1
    cur = 1
    while True:
        for i in range(left, right + 1):
            res[up][i] = cur
            cur += 1
        if up > down - 1: break
        up += 1

        for j in range(up, down + 1):
            res[j][right] = cur
            cur += 1
        if right - 1 < left: break
        right -= 1

        for i in range(right, left - 1, -1):
            res[down][i] = cur
            cur += 1
        if down - 1 < up: break
        down -= 1

        for j in range(down, up - 1, -1):
            res[j][left] = cur
            cur += 1
        if left + 1 > right: break
        left += 1

    return res

print(generateMatrix(5))