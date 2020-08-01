class solution:
    def expand(self, S):
        result = []
        self._expand(S, "", result)
        return result

    def _expand(self, S, prefix, result):
        if not S:
            result.append(prefix)
            return

        if S[0] == '{':
            last_bracket = S.find('}')
            parts = S[1:last_bracket].split(',')
            for part in sorted(parts):
                self._expand(S[last_bracket+1:], prefix+part, result)

        else:
            self._expand(S[1:], prefix + S[0], result)

obj = solution()
S =  "{a,b}c{d,e}f"
print(obj.expand(S))