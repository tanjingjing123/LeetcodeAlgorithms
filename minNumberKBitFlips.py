def minKBitFlips(A, K):
    n = len(A)
    ans = 0
    flip = [0] * n
    x = 0
    for i in range(n):
        if i >= K:
            if flip[i - K] == 1:
                x -= 1
        if not A[i] ^ x % 2:
            if i + K > n:
                return -1
            flip[i] = 1
            x += 1
            ans += 1
    return ans


A = [0,0,0,1,0,1,1,0]  #,1,1,0,0,1,0,0
K = 3
print(minKBitFlips(A, K))