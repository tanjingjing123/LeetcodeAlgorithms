import numpy as np

def forward_elimination(A, b, n):

    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i,row] / A[row,row]
            for j in range(row, n):
                A[i,j] = A[i,j] - factor * A[row,j]

            b[i] = b[i] - factor * b[row]

        print('A = \n%s \nb = \n%s\n' % (A,b))
    return A, b

def back_substitution(a, b, n):

    x = np.zeros((n,1))
    x[n-1] = b[n-1] / a[n-1, n-1]
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row,j] * x[j]
        x[row] = sums / a[row,row]
    return x

def gauss(A, b):

    n = A.shape[0]

    # Check for zero diagonal elements
    if any(np.diag(A)==0):
        raise ZeroDivisionError(('Division by zero will occur; '
                                  'pivoting currently not supported'))

    A, b = forward_elimination(A, b, n)
    return back_substitution(A, b, n)

# Main program starts here

A = np.array([[2, -1, 1],[4, 1, -1], [1, 1, 1]])
b = np.array([1, 5, 0])
x = gauss(A, b)
print('\nGauss result is x = \n %s' % x)