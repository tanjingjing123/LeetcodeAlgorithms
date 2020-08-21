"""# CS483_HW#1_Q3"""

import numpy as np

row_x = [[1], [3], [5], [7], [9], [11], [13], [15], [17], [19]]
x = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [1, 11], [1, 13], [1, 15], [1, 17], [1, 19]]
x = np.array(x)
# print(x)
X = x.transpose()  # x(T)
# print(X)
a = X.dot(x)  # x(T)*x
# print(a)
inverse = np.linalg.inv(a)  # (x(T)*x)^(-1)
# print(inverse)
b = inverse.dot(X)  # (x(T)*x)^(-1)*x(T)
# print(b)
y = [[3], [3], [7], [7], [11], [11], [15], [15], [19], [19]]
theta = b.dot(y)  # (x(T)x)^-1*x(T)*y
print(theta[0], theta[1])


def function(x):
    return theta[0] + theta[1] * x


h = function(row_x)
import matplotlib.pyplot as plt

plt.scatter(row_x, y)
plt.plot(row_x, h, color='red', linewidth=2)
plt.show()