from numpy import matrix
from numpy import linalg

A = matrix([[1,3,3],[1,4,3],[1,3,4]])
x = matrix([[1],[2],[3]])
y = matrix([[1,2,3]])
print(A.T)                                    # Transpose of A.
print(A*x)                                    # Matrix multiplication of A and x.
print(A.I)                                    # Inverse of A.
print(linalg.solve(A, x))