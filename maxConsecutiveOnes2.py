import collections
def longestOnes(A, K):
    i, j = 0, 0
    cnt = 0
    ans = 0
    while j < len(A):
        if cnt <= K and A[j] == 0:
            cnt += 1
        if cnt > K:
            ans = max(ans, (j - i))
            if A[i] == 0:
                cnt -= 1
            i += 1
        if cnt <= K:
            j += 1
    ans = max(ans, j - i)
    return ans


A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(longestOnes(A, K))

