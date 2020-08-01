class solution:
    def function(self, x):
        return x * x - 1000 * x + 1

    def derivFunction(self, x):
        return 2 * x - 1000

    def NewtonRaphson(self, x):
        h = self.function(x) / self.derivFunction(x)

        while abs(h) >= 0.0001:
            h = self.function(x)/self.derivFunction(x)
            x = x - h
        x2 = 1000 - x

        print("The value of the root is: ", "%.4f" % x, "and", "%.4f" % x2)

x = 1000
mysolution = solution()
mysolution.NewtonRaphson(x)
