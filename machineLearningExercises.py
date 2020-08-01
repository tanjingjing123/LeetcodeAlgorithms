# Implementation of gradient descent in linear regression
import numpy as np
import matplotlib.pyplot as plt


class Linear_Regression:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.b = [0] * (len(X) + 1)

    def update_coeffs(self, learning_rate):
        Y_pred = self.predict()
        Y = self.Y
        m = len(Y)
        self.b[0] = self.b[0] - (learning_rate * ((1 / m) *
                                                  np.sum(Y_pred - Y)))
        for i in range(len(self.b) - 1):
            tmp = 0
            for j in range(len(self.b) - 1):
                tmp += (Y_pred[j] - Y[j]) * sum(self.X[j])
            self.b[i + 1] = self.b[i + 1] - (learning_rate * ((1 / m) * tmp))

    def predict(self, X=[]):
        Y_pred = np.array([])
        if not X:
            X = self.X
        b = self.b

        for j in range(len(X[0])):
            result = b[0]
            for i in range(len(X)):
                result += b[i + 1] * X[i][j]
            Y_pred = np.append(Y_pred, result)

        return Y_pred

    def get_current_accuracy(self, Y_pred):
        p, e = Y_pred, self.Y
        n = len(Y_pred)
        return 1 - sum(
            [
                abs(p[i] - e[i]) / e[i]
                for i in range(n)
                if e[i] != 0]
        ) / n
        # def predict(self, b, yi):

    def compute_cost(self, Y_pred):
        m = len(self.Y)
        J = (1 / 2 * m) * (np.sum(Y_pred - self.Y) ** 2)
        return J

    def plot_best_fit(self, Y_pred, fig):
        f = plt.figure(fig)
        plt.scatter(self.X[0], self.Y, color='b')
        plt.plot(self.X[0], Y_pred, color='g')
        f.show()


def main():
    X = np.array([[8, 5, 1, 8, 7, 4, 4, 10, 6, 7, 10, 3, 8, 1, 5, 3, 5, 2, 1, 3, 2, 10, 2, 3, 2, 10, 6, 5, 2, 10, 6, 5],
                  [10, 3, 1, 7, 4, 1, 1, 7, 1, 3, 5, 1, 4, 1, 2, 2, 1, 1, 1, 1, 1, 7, 1, 1, 1, 10, 2, 4, 5, 4, 10, 6],
                  [10, 3, 1, 5, 6, 1, 1, 7, 1, 2, 5, 1, 5, 1, 3, 1, 1, 1, 3, 1, 1, 7, 1, 2, 1, 10, 1, 4, 3, 3, 10, 5],
                  [8, 3, 1, 10, 4, 1, 1, 6, 1, 10, 3, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 8, 1, 9, 3, 1, 2, 6],
                  [7, 2, 2, 7, 6, 2, 2, 4, 2, 5, 6, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 8, 2, 2, 2, 6, 1, 2, 6, 3, 8, 10],
                  [10, 3, 3, 9, 1, 1, 1, 10, 1, 10, 7, 1, 5, 1, 7, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 10, 7, 3, 10, 1],
                  [9, 4, 3, 5, 4, 2, 3, 4, 3, 5, 7, 2, 7, 3, 3, 2, 2, 2, 1, 2, 3, 7, 3, 2, 2, 8, 7, 5, 7, 6, 7, 3],
                  [7, 4, 1, 5, 3, 1, 1, 1, 1, 4, 10, 1, 3, 1, 6, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 9, 1, 6, 5, 5, 3, 1],
                  [1, 1, 1, 4, 1, 1, 1, 2, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1]])
    Y = np.array([4, 4, 2, 4, 4, 2, 2, 4, 2, 4, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 4, 2, 4, 4, 4, 4, 4])

    regressor = Linear_Regression(X, Y)

    iterations = 0
    steps = 100
    learning_rate = 0.01
    costs = []

    # original best-fit line
    Y_pred = regressor.predict()
    regressor.plot_best_fit(Y_pred, 'Initial Best Fit Line')

    while 1:
        Y_pred = regressor.predict()
        cost = regressor.compute_cost(Y_pred)
        costs.append(cost)
        regressor.update_coeffs(learning_rate)

        iterations += 1
        if iterations % steps == 0:
            print(iterations, "epochs elapsed")
            print("Current accuracy is :",
                  regressor.get_current_accuracy(Y_pred))

            stop = input("Do you want to stop (y/*)??")
            if stop == "y":
                break

    # final best-fit line
    regressor.plot_best_fit(Y_pred, 'Final Best Fit Line')

    # plot to verify cost fuction decreases
    h = plt.figure('Verification')
    plt.plot(range(iterations), costs, color='b')
    h.show()

    # if user wants to predict using the regressor:
    regressor.predict([i for i in range(10)])


if __name__ == '__main__':
    main()