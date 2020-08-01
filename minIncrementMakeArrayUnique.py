def minIncrement(A):
    A.sort()
    last = -float('inf')
    ans = 0

    for x in A:
        if x <= last:
            ans += (last + 1 - x)
            last = (last + 1)
        else:
            last = x

    return ans

A =  [3,2,1,2,1,7]
print(minIncrement(A))