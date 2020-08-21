def rotate90Clockwise(matrix):
    n = len(matrix[0])
    for i in range(n//2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp

def printMatrix(matrix):
    n = len(matrix[0])
    for i in range(n):
        print(matrix[i])


matrix = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

rotate90Clockwise(matrix)
printMatrix(matrix)