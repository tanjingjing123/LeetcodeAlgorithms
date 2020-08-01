class solution:
    def generateAbbre(self, word):
        res = []
        self.dfs(word, [], 0, 0, res)
        return res

    def dfs(self, word, cur, pos, cnt, res):
        if pos == len(word):
            if cnt:
                cur.append(str(cnt))
            res.append("".join(cur))
            return

        self.dfs(word, cur, pos + 1, cnt + 1, res)
        cur.pop()

        if cnt:
            cur.append(str(cnt))

        self.dfs(word, cur + [word[pos]], pos + 1, 0, res)

obj = solution()
print(obj.generateAbbre("word"))