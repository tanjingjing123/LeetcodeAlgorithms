import math

def find_prime(x, y):
    res = []
    for num in range(x, y + 1):
        if num < 2:
            continue
        if num == 2:
            res.append(num)
        else:
            sqrt_num = math.floor(math.sqrt(num))
            insertFlag = True
            for found in res:
                if found > sqrt_num:
                    break
                if num % found == 0:
                    insertFlag = False
                    break
            if insertFlag:
                res.append(num)
    return res

prime_res = find_prime(2, 20)
print(prime_res)