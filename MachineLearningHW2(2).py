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
            dtheta1 = dtheta1 + (
                        1 / (1 + np.exp(-(theta1 * x[0] + theta2 * x[1] * x[1]))) - x[2]) * x[0]
            dtheta2 = dtheta2 + (
                        1 / (1 + np.exp(-(theta1 * x[0] + theta2 * x[1] * x[1]))) - x[2]) * 2 * \
                      x[1]

        theta1 = theta1 - alpha * dtheta1 / m
        theta2 = theta2 - alpha * dtheta2 / m

        iteration -= 1

    return (theta1, theta2)


'''
def pred(training_set,test_set):
  (t1,t2,t3)=training(training_set)
  #print(t1,t2,t3)
  return 1/(1+np.exp(-(t1*test_set[0]+t2*test_set[1]*test_set[1]+t3*test_set[2]*test_set[2])))
'''

tr = [[-3.98, -0.12, 1], [-3.464, -2.11, 1], [-3.461, 1.89, 1], [-2.22, -3.474, 1], [-2.02, 0.03, 0],
      [-2.01, 3.459, 1], [-1.42, -1.409, 0], [-1.416, 1.419, 0], [-1.09, 0.08, 0], [-0.19, -4.13, 1],
      [-1.42, -1.409, 0], [-1.416, 1.419, 0], [-1.09, 0.08, 0], [0.06, 3.97, 1], [0.07, 0.1, 0],
      [0.12, -1.12, 0], [1.11, 0.09, 0], [1.411, 1.419, 0], [1.414, -1.415, 0], [1.86, 3.47, 1],
      [1.96, -0.12, 0], [2.11, -3.472, 1], [3.461, -1.87, 1], [3.464, 2.07, 1], [4.12, 0.09, 1]]
tr = np.array(tr)  # matrix format
tr[:, 0] = (tr[:, 0] - min(tr[:, 0])) / (max(tr[:, 0]) - min(tr[:, 0]))  # normalization bwt 0~1
tr[:, 1] = (tr[:, 1] - min(tr[:, 1])) / (max(tr[:, 1]) - min(tr[:, 1]))  # normalization bwt 0~1

(t1, t2) = training(tr)
print(t1, t2)

import matplotlib.pyplot as plt

# the row which Y=1
row_x1 = [[-3.98, -0.12], [-3.464, -2.11], [-3.461, 1.89], [-2.22, -3.474], [-2.01, 3.459], [-0.19, -4.13],
          [0.06, 3.97], [1.86, 3.47], [2.11, -3.472], [3.461, -1.87], [3.464, 2.07], [4.12, 0.09]]

# the row which Y=0
row_x2 = [[-2.02, 0.03], [-1.42, -1.409], [-1.416, 1.419], [-1.09, 0.08], [-1.42, -1.409], [-1.416, 1.419],
          [-1.09, 0.08], [0.07, 0.1], [0.12, -1.12], [1.11, 0.09], [1.411, 1.419], [1.414, -1.415], [1.96, -0.12]]

for x in row_x1:
    plt.scatter(x[0], x[1], color='blue')

for x in row_x2:
    plt.scatter(x[0], x[1], color='red')
plt.show()
