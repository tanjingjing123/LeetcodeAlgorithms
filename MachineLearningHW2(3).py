import numpy as np


def training(tr_set):
    '''
      Description: tr_set -> multi dimension list for each training sample, like (1,x1,x2,y)
    '''
    (theta1, theta2) = (0, 0)  # Initialize theta's value
    alpha = 0.01  # Set up learning rate
    m = len(tr_set)  # Get number of samples in training set
    iteration = 36000
    while iteration > 0:
        dtheta1 = 0  # Initialize derivative value to big enough
        dtheta2 = 0
        for x in tr_set:  # x[0]=x0; x[1]=x1; x[2]=x2; x[3]=y
            dtheta1 = dtheta1 + (1 / (1 + np.exp(-(theta1 * x[0] + theta2 * x[1]))) - x[2]) * x[0]
            dtheta2 = dtheta2 + (1 / (1 + np.exp(-(theta1 * x[0] + theta2 * x[1]))) - x[2]) * x[1]

        theta1 = theta1 - alpha * dtheta1 / m
        theta2 = theta2 - alpha * dtheta2 / m

        iteration -= 1

    return (theta1, theta2)


def pred(training_set, test_set):
    '''Description: test_set-list data type with programmin score & ML score pred function return value is probability of getting job offer
    '''
    (t1, t2) = training(training_set)
    print(t1, t2)
    return 1 / (1 + np.exp(-(t1 * test_set[0] + t2 * test_set[1])))


# y=2
tr1 = [[3.25, 7.956, 1], [3.3, 2.2, 0], [3.32, 3.41, 0], [3.35, 10.272, 1], [4.01, 1.65, 0],
       [4.03, 2.51, 0], [4.05, 4.21, 0], [4.05, 7.38, 1], [4.06, 11.412, 1], [4.07, 9.198, 1],
       [5.22, 2.15, 0], [5.24, 3.41, 0], [5.25, 7.866, 1], [5.28, 10.008, 1], [8.15, 6.3, 0],
       [8.23, 7.95, 0], [9.38, 7.34, 0], [9.4, 8.21, 0], [10.2, 6.52, 0], [10.8, 7.72, 0]]

# y=1
tr2 = [[3.25, 7.956, 0], [3.3, 2.2, 0], [3.32, 3.41, 0], [3.35, 10.272, 0], [4.01, 1.65, 0],
       [4.03, 2.51, 0], [4.05, 4.21, 0], [4.05, 7.38, 0], [4.06, 11.412, 0], [4.07, 9.198, 0],
       [5.22, 2.15, 0], [5.24, 3.41, 0], [5.25, 7.866, 0], [5.28, 10.008, 0], [8.15, 6.3, 1],
       [8.23, 7.95, 1], [9.38, 7.34, 1], [9.4, 8.21, 1], [10.2, 6.52, 1], [10.8, 7.72, 1]]

# y=0
tr3 = [[3.25, 7.956, 0], [3.3, 2.2, 1], [3.32, 3.41, 1], [3.35, 10.272, 0], [4.01, 1.65, 1],
       [4.03, 2.51, 1], [4.05, 4.21, 1], [4.05, 7.38, 0], [4.06, 11.412, 0], [4.07, 9.198, 0],
       [5.22, 2.15, 1], [5.24, 3.41, 1], [5.25, 7.866, 0], [5.28, 10.008, 0], [8.15, 6.3, 0],
       [8.23, 7.95, 0], [9.38, 7.34, 0], [9.4, 8.21, 0], [10.2, 6.52, 0], [10.8, 7.72, 0]]

tr1 = np.array(tr1)  # matrix format
# tr1[:,1]=(tr1[:,1] - min(tr1[:,1] )) / (max(tr1[:,1])-min(tr1[:,1]))  # normalization bwt 0~1
# tr1[:,2]=(tr1[:,2] - min(tr1[:,1] )) / (max(tr1[:,2])-min(tr1[:,2]))  # normalization bwt 0~1

tr2 = np.array(tr2)  # matrix format
# tr2[:,1]=(tr2[:,1] - min(tr2[:,1] )) / (max(tr2[:,1])-min(tr2[:,1]))  # normalization bwt 0~1
# tr2[:,2]=(tr2[:,2] - min(tr2[:,1] )) / (max(tr2[:,2])-min(tr2[:,2]))  # normalization bwt 0~1

tr3 = np.array(tr3)  # matrix format
# tr3[:,1]=(tr3[:,1] - min(tr3[:,1] )) / (max(tr3[:,1])-min(tr3[:,1]))  # normalization bwt 0~1
# tr3[:,2]=(tr3[:,2] - min(tr3[:,1] )) / (max(tr3[:,2])-min(tr3[:,2]))  # normalization bwt 0~1


predict1 = [4.01, 3.02]
print(pred(tr1, predict1), "---", pred(tr2, predict1), "---", pred(tr3, predict1), "\n")

predict2 = [9.1, 6.5]
print(pred(tr1, predict2), "---", pred(tr2, predict2), "---", pred(tr3, predict2), "\n")

predict3 = [3.50, 9.50]
print(pred(tr1, predict3), "---", pred(tr2, predict3), "---", pred(tr3, predict3), "\n")

predict4 = [1, 6.01, 6.01]
print(pred(tr1, predict4), "---", pred(tr2, predict4), "---", pred(tr3, predict4), "\n")

import matplotlib.pyplot as plt

# the row which Y=2
row_x1 = [[3.25, 7.956], [3.35, 10.272], [4.05, 7.38], [4.06, 11.412], [4.07, 9.198], [5.25, 7.866], [5.28, 10.008],
          [9.1, 6.5], [3.5, 9.5]]

# the row which Y=1
row_x2 = [[8.15, 6.3], [8.23, 7.95], [9.38, 7.34], [9.4, 8.21], [10.2, 6.52], [10.8, 7.72], [6.01, 6.01]]

# the row which Y=0
row_x3 = [[3.3, 2.2], [3.32, 3.41], [4.01, 1.65], [4.03, 2.51], [4.05, 4.21], [5.22, 2.15], [5.24, 3.41], [4.01, 3.02]]

for x in row_x1:
    plt.scatter(x[0], x[1], color='blue')

for x in row_x2:
    plt.scatter(x[0], x[1], color='red')

for x in row_x3:
    plt.scatter(x[0], x[1], color='Green')

plt.show()