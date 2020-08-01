import random


class solution:
    def __init__(self, w):
        s = sum(w)
        self.weight = [w[0] / s]
        for i in range(1, len(w)):
            self.weight.append(self.weight[-1] + w[i]/s)

    def pickIndex(self):
        l, r, seed = 0, len(self.weight)-1, random.random()
        while l < r:
            m = (l + r) // 2
            if self.weight[m] <= seed:
                l = m + 1
            else:
                r = m
        return l

w= [1, 8, 9, 3, 6]
obj = solution(w)
print(obj.pickIndex())