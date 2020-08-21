import numpy as np


def training(tr_set):
    theta1 = 0  # Initialize theta's value
    alpha = 0.01  # Set up learning rate
    m = len(tr_set)  # Get number of samples in training set
    iteration = 36000
    while iteration > 0:
        dtheta1 = 0  # Initialize derivative value to big enough
        for x in tr_set:  # x[0]=x0; x[1]=y
            dtheta1 = dtheta1 + ((theta1 * x[0]) - x[1]) * x[0]

        theta1 = theta1 - alpha * dtheta1 / m

        iteration -= 1

    return theta1


def pred(training_set, test_set):
    t1= training(training_set)
    return t1 * test_set[0]


def normalized(arr):
    minV = min(arr)
    maxV = max(arr)
    avg = sum(arr) / len(arr)
    for i, c in enumerate(arr):
        arr[i] = (c - avg) / (maxV - minV)


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 16, 21, 36, 45, 64, 77, 100, 117, 144]

normalized(x)
normalized(y)

tr = zip(x, y)
tr = []
for i in range(len(x)):
    tr.append([x[i], y[i]])
tr = np.array(tr)
predicted = []
for line in tr:
    result = (pred(tr, line) * 140 + 57.18181818)
    predicted.append(result)


row_x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
row_y = [[4], [5], [16], [21], [36], [45], [64], [77], [100], [117], [144]]

# def function(x):
# return t1[0] + t2[0]*x

# h=function(row_x)
import matplotlib.pyplot as plt

plt.scatter(row_x, row_y)
plt.scatter(row_x, predicted)
plt.plot(row_x, row_y, color='red', linewidth=2)
plt.plot(row_x, predicted, color='blue', linewidth=2)
plt.show()

