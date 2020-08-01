class solution:
    def confusingNumber2(self, N):
        def dfs(n, rotate, digit, res):
            if n != rotate:
                res.append(n)
            for d in confuse:
                num = n * 10 + d
                if num > N:
                    return
                dfs(num, confuse[d] * digit + rotate, digit * 10, res)

        confuse, res = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}, []
        for d in confuse:
            if d != 0:
                dfs(d, confuse[d], 10, res)
        return len(res)


obj = solution()
N = 20
print(obj.confusingNumber2(N))
