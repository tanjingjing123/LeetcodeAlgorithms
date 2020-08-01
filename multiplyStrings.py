def multiply(num1, num2):
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    a = 0
    b = 0
    for i in num1:
        a = a * 10 + d[i]
    for j in num2:
        b = b * 10 + d[j]
    return str(a * b)

num1 = "123"
num2 = "456"
print(multiply(num1, num2))