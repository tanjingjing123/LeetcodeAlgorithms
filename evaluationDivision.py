class Solution:
    def find(self, x, UF):
        if x != UF[x][0]:
            px, pv = self.find(UF[x][0], UF)
            UF[x] = (px, UF[x][1] * pv)
        return UF[x]

    def divide(self, x, y, UF):
        rx, vx = self.find(x, UF)
        ry, vy = self.find(y, UF)
        if rx != ry: return -1.0
        return vx / vy

    def calcEquation(self, equations, values, queries):
        UF = {}
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            if x not in UF and y not in UF:
                UF[x] = (y, value)
                UF[y] = (y, 1.0)
            elif x not in UF:
                UF[x] = (y, value)
            elif y not in UF:
                UF[y] = (x, 1.0 / value)
            else:
                rootx, valx = self.find(x, UF)
                rooty, valy = self.find(y, UF)
                UF[rootx] = (rooty, value * valy / valx)

        res = []
        for x, y in queries:
            # from x to y
            if all(i in UF for i in (x, y)):
                res.append(self.divide(x, y, UF))
            else:
                res.append(-1.0)
        return res

obj = Solution()
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(obj.calcEquation(equations, values, queries))