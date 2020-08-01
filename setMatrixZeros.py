def setZeros(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows:
                matrix[i][j] == 0
            if j in cols:
                matrix[i][j] = 0


matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
setZeros(matrix)