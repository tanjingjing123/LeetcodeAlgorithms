def findDiagonalOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = []
    for k in range(m+n-1):
            if k % 2:
                for i in range(0, n):
                    res.append(matrix[i][k-i])

            else:
                for i in range(0, k+1):
                    res.append(matrix[k-i][i])
    return res

matrix = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
print(findDiagonalOrder(matrix))
