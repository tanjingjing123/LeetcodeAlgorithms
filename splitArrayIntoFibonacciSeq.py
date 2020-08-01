class solution:
    def splitIntoFibonacci(self, S):
        MAX = pow(2, 31) - 1
        self.res = []

        def back(path, start):
            if start >= len(S) and len(path) > 2:
                self.res = path
                return

            for i in range(start, len(S)):
                cur = S[start: i + 1]
                cur_len = len(cur)

                if cur_len > 1 and cur[0] == '0':
                    break

                if int(cur) > MAX:
                    break

                if len(path) < 2:
                    back(path + [int(cur)], i + 1)
                else:
                    if int(cur) == (path[-1] + path[-2]):
                        back(path + [int(cur)], i+1)
        back([], 0)
        return self.res
obj = solution()
S = "1101111"
print(obj.splitIntoFibonacci(S))