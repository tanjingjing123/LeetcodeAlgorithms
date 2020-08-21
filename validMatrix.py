def isValidMatrix(matrix):
    if not matrix:
        return False

    n = len(matrix)
    for i in range(n):
        rowSet = set()
        colSet = set()
        rowMin = float('inf')
        rowMax = float('-inf')
        colMin = rowMin
        colMax = rowMax

        for j in range(n):
            if matrix[i][j] not in rowSet:
                rowSet.add(matrix[i][j])
                rowMin = min(rowMin, matrix[i][j])
                rowMax = max(rowMax, matrix[i][j])
            else:
                return False

            if matrix[j][i] not in colSet:
                colSet.add(matrix[j][i])
                colMin = min(colMin, matrix[j][i])
                colMax = max(colMax, matrix[j][i])
            else:
                return False

        if rowMin != 1 or colMin != 1 or rowMax != n or colMax != n:
            return False

    return True

matrix = [[3, 2, 4, 1, 5], [4, 1, 5, 3, 2],[1, 5, 3, 2, 4],[2, 4, 1, 5, 3],[5, 3, 2, 4, 1]]
print(isValidMatrix(matrix))