
def getFactors(n):
    def rec(v, i):
        paths = []
        while i*i <= v:
            if v % i == 0:
                paths.append([i, v//i])
                for p in rec(v//i, i):
                    paths.append([i] + p)
            i += 1
        return paths
    result = rec(n, 2)
    return result
n = 60
print(getFactors(n))