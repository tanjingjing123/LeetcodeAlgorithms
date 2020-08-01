from math import factorial
from math import ceil
class solution:
    def getPermutation(self, n, k):
        ans = []
        stuff = list(map(str, range(1, n + 1)))
        self.fill(n, k, ans, stuff)
        return ''.join(ans)

    def fill(self, n, k, ans, stuff):
        if n > 0:
            x = factorial(n - 1)
            ans.append(stuff.pop(ceil(k/x)-1))
            self.fill(n - 1, k % x, ans, stuff)
        else:
            return

n = 4
k = 9
obj = solution()
print(obj.getPermutation(n, k))