def multiply(A, B):
    row = len(A)
    col = len(B[0])
    res = [[0] * col for i in range(row)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != 0:
                for k in range(len(B[0])):
                    if B[j][k] != 0:
                        res[i][k] += A[i][j] * B[j][k]

    return res

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
print(multiply(A, B))