def countStepping(low, high):
    res = []
    if low == 0:
        res.append(0)

    stack = list(range(1, 10))
    while stack:
        num = stack.pop(0)
        if low <= num <= high:
            res.append(num)

        lastdigit = num % 10
        num = num * 10

        if num < high:
            if lastdigit != 0:
                stack.append(num + lastdigit - 1)
            if lastdigit != 9:
                stack.append(num + lastdigit + 1)

    return (res)

low = 100
high = 2000
print(countStepping(low, high))