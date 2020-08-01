def minSwap(A, B):
    n = len(A)
    x = 0
    y = 0
    for i in range(1, len(dp)):
        new_x = 1001
        new_y = 1001
        if A[i] > A[i-1] and B[i] > B[i-1]:
            new_x = min(new_x, x)
            new_y = min(new_y, y+1)

        if A[i] > B[i-1] and B[i] > A[i-1]:
            new_x = min(new_x, y)
            new_y = min(new_y, x+1)
        x = new_x
        y = new_y


    return min(dp[-1])

A = [1,3,5,4]
B = [1,2,3,7]
print(minSwap(A, B))
