def maxSideLength(mat, threshold):
    n, m = len(mat), len(mat[0])
    presum = [[0 for j in range(m + 1)] for i in range(n + 1)]
    maxSideLen = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            presum[i][j] = presum[i - 1][j] + presum[i][j - 1] + mat[i - 1][j - 1] - presum[i - 1][j - 1]
            k = maxSideLen + 1
            # check the square with len K form by current i,j (as lower right)
            if j >= k and i >= k:
                cursum = presum[i][j] - presum[i][j - k] - presum[i - k][j] + presum[i - k][j - k]
                if cursum <= threshold:
                    maxSideLen = k
    return maxSideLen

mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 6
print(maxSideLength(mat, threshold))