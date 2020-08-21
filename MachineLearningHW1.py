import numpy as np


# hypothesishypothesis function ---- h(theta)=theta1+theta2*x
# loss function    ------ l=[h(x(i))-y(i)]^2
# cost function    ------ J(theta) = [h(x(i))-y(i)]^2/(2*m)

def training(tr_set):
    (theta1, theta2) = (0, 0)  # Initialize theta's value
    alpha = 0.01  # Set up learning rate
    m = len(tr_set)  # Get number of samples in training set
    iteration = 36000
    while iteration > 0:
        dtheta1 = 0  # Initialize derivative value to big enough
        dtheta2 = 0
        for x in tr_set:  # x[0]=x0; x[1]=x1; x[2]=y
            dtheta1 = dtheta1 + ((theta1 * x[0] + theta2 * x[1]) - x[2]) * x[0]
            dtheta2 = dtheta2 + ((theta1 * x[0] + theta2 * x[1]) - x[2]) * x[1]

        theta1 = theta1 - alpha * dtheta1 / m
        theta2 = theta2 - alpha * dtheta2 / m

        iteration -= 1

    return (theta1, theta2)


def pred(training_set, test_set):
    (t1, t2) = training(training_set)
    return t1 * test_set[0] + t2 * test_set[1]


def normalized(arr):
    minV = min(arr)
    maxV = max(arr)
    avg = sum(arr) / len(arr)
    for i, c in enumerate(arr):
        arr[i] = (c - avg) / (maxV - minV)


sbp = [117, 120, 145, 129, 132, 130, 110, 163, 136, 115, 118, 132, 111, 112]
weight = [58, 90, 96, 72, 62, 79, 69, 96, 96, 54, 67, 99, 74, 73]
age = [60, 61, 74, 57, 63, 68, 66, 77, 63, 54, 63, 76, 60, 61]
testMatrix = [[(65 - sum(age) / len(age)) / (max(age) - min(age)),
               (85 - sum(weight) / len(weight)) / (max(weight) - min(weight))],
              [(79 - sum(age) / len(age)) / (max(age) - min(age)),
               (80 - sum(weight) / len(weight)) / (max(weight) - min(weight))]]
testMatrix = np.array(testMatrix)
normalized(sbp)
normalized(weight)
normalized(age)
print("SBP normalized:", sbp)
print("weight normalized:", weight)
print("age normalized:", age)

trMatrix = []
for i in range(len(sbp)):
    trMatrix.append([age[i], weight[i], sbp[i]])

trMatrix = np.array(trMatrix)

for line in testMatrix:
    result = pred(trMatrix, line)
    print("After training: ", result, "\npredict value: ", result * 53 + 126.4285714)
