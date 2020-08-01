def maxTurbulent(A):
    rst, l = 1, 0
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            l = i
        elif i - 2 >= 0 and not ((A[i-2] < A[i-1]) ^ (A[i-1] < A[i])):
            l = i - 1
        rst = max(rst, i - l + 1)
    return rst


nums = [9,4,2,3,4,5,8,10,19]
print(maxTurbulent(nums))