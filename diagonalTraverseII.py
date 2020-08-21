def findDiagonalOrder(matrix):
    col = 0
    row = 0
    res = []
    isRc = False
    while row < len(matrix):
        i = row
        j = col
        temp = []
        while i < len(matrix) and i >= 0 and j < len(matrix[0]) and j >= 0:
            temp.append(matrix[i][j])
            i += 1
            j -= 1
        if col < len(matrix[0]) - 1:
            col += 1
        else:
            row += 1
        if isRc:
            res.extend(temp)
            isRc = False
        else:
            res.extend(temp[::-1])
            isRc = True
    return res


matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
print(findDiagonalOrder(matrix))