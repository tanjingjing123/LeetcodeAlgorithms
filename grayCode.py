def grayCode(n):
    if n == 0:
        return [0]

    nums = ["0" * n]
    for i in range(n):
        tmp = []
        for j in nums[::-1]:
            if j[i] == "1":
                tmp.append(j[:i] + "0" + j[i+1:])
            else:
                tmp.append(j[:i] + "1" + j[i+1:])
        nums += tmp

    return [int(i, 2) for i in nums]

print(grayCode(4))