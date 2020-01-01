def basicCal(expression):
    if not expression:
        return 0
    expression = list(expression)

    result = 0
    sign = 1
    i = 0
    while i < len(expression):
        if expression[i].isnumeric():
            num = expression[i]
            while i + 1 < len(expression) and expression[i+1].isnumeric():
                num += expression[i+1]
                i += 1
            num = int(num)
            i += 1
            result += num * sign
        elif expression[i] == '+':
            sign = 1
            i += 1
        elif expression[i] == '-':
            sign = -1
            i += 1


    return result

expression = "2+13-999"
print(basicCal(expression))
