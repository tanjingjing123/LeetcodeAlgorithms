def maxSumTwoNoOverlap(A, L, M):
    if len(A) < L + M:
        return 0
    for i in range(1, len(A)):
        A[i] += A[i-1]

    res, maxL, maxM = A[L+M-1],A[L-1], A[M-1]
    for i in range(L+M, len(A)):
        maxL = max(maxL, A[i-M] - A[i-M-L])
        maxM = max(maxM, A[i-L] - A[i-L-M])
        res = max(res, maxL + A[i]-A[i-M], maxM + A[i] - A[i-L])
    return res



A = [2,1,5,6,0,9,5,0,3,8]
L = 4
M = 3
print(maxSumTwoNoOverlap(A, L, M))