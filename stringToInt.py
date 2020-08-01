def myAtoi(str):
    str = str.strip(' ')
    res = []
    for i in str:
        if (i == '-' or i == '+') and len(res) == 0:
            res.append(i)
        elif i.isnumeric():
            res.append(i)
        else:
            break

    if len(res) == 0 or res == ['+'] or res == ['-']:
        return 0
    else:
        str = ''.join(res)
        number = int(str, 10)
        if number < -2 ** 31:
            return -2**31
        elif number > 2 ** 31 - 1:
            return 2**31 - 1
        else:
            return number
s = "   -987"
print(myAtoi(s))