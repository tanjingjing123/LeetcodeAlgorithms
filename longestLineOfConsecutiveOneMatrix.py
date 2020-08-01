def longest(M):
    if not M or not M[0]:
        return 0
    m, n = len(M), len(M[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if M[i][j] == 1:
                if i == 0 or M[i-1][j] != 1:
                    k, cur = 1, 1
                    while k+i < m and M[k+i][j] == 1:
                        cur, k = cur+1, k+1
                    res = max(res, cur)
                if j == 0 or M[i][j-1] != 1:
                    k, cur = 1, 1
                    while k+j < n and M[i][k+j] == 1:
                        cur, k = cur + 1, k + 1
                    res = max(res, cur)
                if i == 0 or j == 0 or M[i-1][j-1] != 1:
                    k, cur = 1, 1
                    while k+i < m and k + j < n and M[k+i][k+j] == 1:
                        cur, k = cur+1, k+1
                    res = max(res, cur)
                if i == 0 or j == n-1 or M[i-1][j+1] != 1:
                    k, cur = 1, 1
                    while k+i<m and j-k>= 0 and M[k+i][j-k] == 1:
                        cur, k = cur+1, k+1
                    res = max(res, cur)
    return res
M = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
print(longest(M))


