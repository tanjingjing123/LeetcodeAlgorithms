def brokenCalculator(X, Y):
    ans = 0
    while Y > X:
        ans += 1
        if Y % 2:
            Y += 1
        else:
            Y  = Y//2
    return ans + X - Y


n = 5
m = 33
print(brokenCalculator(n, m))
