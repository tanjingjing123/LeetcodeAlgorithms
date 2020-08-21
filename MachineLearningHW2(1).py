import numpy as np


def training(tr_set):
    (theta1, theta2, theta3, theta4, theta5, theta6, theta7, theta8, theta9) = (
    0, 0, 0, 0, 0, 0, 0, 0, 0)  # Initialize theta's value
    alpha = 0.01  # Set up learning rate
    m = len(tr_set)  # Get number of samples in training set
    iteration = 36000
    while iteration > 0:
        dtheta1 = 0  # Initialize derivative value to big enough
        dtheta2 = 0
        dtheta3 = 0
        dtheta4 = 0
        dtheta5 = 0
        dtheta6 = 0
        dtheta7 = 0
        dtheta8 = 0
        dtheta9 = 0
        for x in tr_set:  # x[0]=x0; x[1]=x1; x[2]=x2 ... x[10]=y
            dtheta1 = dtheta1 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[0]
            dtheta2 = dtheta2 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[1]
            dtheta3 = dtheta3 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[2]
            dtheta4 = dtheta4 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[3]
            dtheta5 = dtheta5 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[4]
            dtheta6 = dtheta6 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[5]
            dtheta7 = dtheta7 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[6]
            dtheta8 = dtheta8 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[7]
            dtheta9 = dtheta9 + (1 / (1 + np.exp(-(
                        theta1 * x[0] + theta2 * x[1] + theta3 * x[2] + theta4 * x[3] + theta5 * x[4] + theta6 * x[
                    5] + theta7 * x[6] + theta8 * x[7] + theta9 * x[8]))) - x[9]) * x[8]

        theta1 = theta1 - alpha * dtheta1 / m
        theta2 = theta2 - alpha * dtheta2 / m
        theta3 = theta3 - alpha * dtheta3 / m
        theta4 = theta4 - alpha * dtheta4 / m
        theta5 = theta5 - alpha * dtheta5 / m
        theta6 = theta6 - alpha * dtheta6 / m
        theta7 = theta7 - alpha * dtheta7 / m
        theta8 = theta8 - alpha * dtheta8 / m
        theta9 = theta9 - alpha * dtheta9 / m

        iteration -= 1

    return (theta1, theta2, theta3, theta4, theta5, theta6, theta7, theta8, theta9)


def pred(training_set, test_set):
    (t1, t2, t3, t4, t5, t6, t7, t8, t9) = training(training_set)
    return 1 / (1 + np.exp(-(
                t1 * test_set[0] + t2 * test_set[1] + t3 * test_set[2] + t4 * test_set[3] + t5 * test_set[4] + t6 *
                test_set[5] + t7 * test_set[6] + t8 * test_set[7] + t9 * test_set[8])))


# set 4 to 0, 2 to 1.
tr = [[8, 10, 10, 8, 7, 10, 9, 7, 1, 0], [5, 3, 3, 3, 2, 3, 4, 4, 1, 0], [1, 1, 1, 1, 2, 3, 3, 1, 1, 1],
      [8, 7, 5, 10, 7, 9, 5, 5, 4, 0], [7, 4, 6, 4, 6, 1, 4, 3, 1, 0], [4, 1, 1, 1, 2, 1, 2, 1, 1, 1],
      [4, 1, 1, 1, 2, 1, 3, 1, 1, 1], [10, 7, 7, 6, 4, 10, 4, 1, 2, 0], [6, 1, 1, 1, 2, 1, 3, 1, 1, 1],
      [7, 3, 2, 10, 5, 10, 5, 4, 4, 0], [10, 5, 5, 3, 6, 7, 7, 10, 1, 0], [3, 1, 1, 1, 2, 1, 2, 1, 1, 1],
      [8, 4, 5, 1, 2, 5, 7, 3, 1, 0], [1, 1, 1, 1, 2, 1, 3, 1, 1, 1], [5, 2, 3, 4, 2, 7, 3, 6, 1, 0],
      [3, 2, 1, 1, 1, 1, 2, 1, 1, 1], [5, 1, 1, 1, 2, 1, 2, 1, 1, 1], [2, 1, 1, 1, 2, 1, 2, 1, 1, 1],
      [1, 1, 3, 1, 2, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 2, 1, 1, 1], [2, 1, 1, 1, 2, 1, 3, 1, 1, 1],
      [10, 7, 7, 3, 8, 5, 7, 4, 3, 0], [2, 1, 1, 2, 2, 1, 3, 1, 1, 1], [3, 1, 2, 1, 2, 1, 2, 1, 1, 1],
      [2, 1, 1, 1, 2, 1, 2, 1, 1, 1], [10, 10, 10, 8, 6, 1, 8, 9, 1, 0], [6, 2, 1, 1, 1, 1, 7, 1, 1, 1],
      [5, 4, 4, 9, 2, 10, 5, 6, 1, 0], [2, 5, 3, 3, 6, 7, 7, 5, 1, 0], [10, 4, 3, 1, 3, 3, 6, 5, 2, 0],
      [6, 10, 10, 2, 8, 10, 7, 3, 3, 0], [5, 6, 5, 6, 10, 1, 3, 1, 1, 0]]
tr = np.array(tr)  # matrix format

tr[:, 0] = (tr[:, 0] - min(tr[:, 0])) / (max(tr[:, 0]) - min(tr[:, 0]))  # normalization bwt 0~1
tr[:, 1] = (tr[:, 1] - min(tr[:, 1])) / (max(tr[:, 1]) - min(tr[:, 1]))  # normalization bwt 0~1
tr[:, 2] = (tr[:, 2] - min(tr[:, 1])) / (max(tr[:, 2]) - min(tr[:, 2]))  # normalization bwt 0~1
tr[:, 3] = (tr[:, 3] - min(tr[:, 1])) / (max(tr[:, 3]) - min(tr[:, 3]))  # normalization bwt 0~1
tr[:, 4] = (tr[:, 4] - min(tr[:, 1])) / (max(tr[:, 4]) - min(tr[:, 4]))  # normalization bwt 0~1
tr[:, 5] = (tr[:, 5] - min(tr[:, 1])) / (max(tr[:, 5]) - min(tr[:, 5]))  # normalization bwt 0~1
tr[:, 6] = (tr[:, 6] - min(tr[:, 1])) / (max(tr[:, 6]) - min(tr[:, 6]))  # normalization bwt 0~1
tr[:, 7] = (tr[:, 7] - min(tr[:, 1])) / (max(tr[:, 7]) - min(tr[:, 7]))  # normalization bwt 0~1
tr[:, 8] = (tr[:, 8] - min(tr[:, 1])) / (max(tr[:, 8]) - min(tr[:, 8]))  # normalization bwt 0~1

(t1, t2, t3, t4, t5, t6, t7, t8, t9) = training(tr)

test1 = [10, 10, 10, 4, 8, 1, 8, 10, 1]
print(pred(tr, test1))

test2 = [6, 6, 6, 9, 6, 2, 7, 8, 1]
print(pred(tr, test2))
