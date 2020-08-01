import itertools
from collections import defaultdict
class solution:
    def generateSentence(self, synonyms, text):
        uf = {}
        def union(x, y):
            uf[find(y)] = find(x)

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        for a, b in synonyms:
            union(a, b)

        d = defaultdict(set)
        for a, b in synonyms:
            root = find(a)
            d[root] |= set([a, b])

        txt = text.split()
        res = []
        for t in txt:
            if t not in uf:
                res.append([t])
            else:
                r = find(t)
                res.append(list(d[r]))
        fin_res = [' '.join(sentence) for sentence in itertools.product(*res)]
        return sorted(fin_res)

obj = solution()
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
print(obj.generateSentence(synonyms, text))
