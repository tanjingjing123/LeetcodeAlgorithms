class Solution:
    def countArrangement(self, N: int) -> int:
        self.cnt = 0
        used = [0] * (N + 1)

        def dfs(s=1):
            if s == N + 1:
                self.cnt += 1
                return

            for i in range(1, N + 1):
                if not used[i] and min(i % s, s % i) == 0:
                    used[i] = 1
                    dfs(s + 1)
                    used[i] = 0

        dfs()
        return self.cnt
obj = Solution()
print(obj.countArrangement(3))