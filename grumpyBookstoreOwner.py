def maxSatisfied(customers, grumpy, X):
    res = can_change = max_can_change = 0
    m = len(grumpy)
    left = 0
    for i in range(m):
        if grumpy[i] == 0:
            res += customers[i]
        else:
            can_change += customers[i]

        if i - left + 1 == X:
            max_can_change = max(max_can_change, can_change)
            if grumpy[left] == 1:
                can_change -= customers[left]
            left += 1
    return res + max_can_change
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(maxSatisfied(customers, grumpy, X))