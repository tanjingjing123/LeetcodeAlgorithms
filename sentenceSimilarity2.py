def areSentenceSimilarTwo(words1, words2, pairs):
    if len(words1) != len(words2):
        return False

    UF = {}
    def find(x):
        if UF[x] != x:
            UF[x] = find(UF[x])
        return UF[x]

    def union(x, y):
        UF.setdefault(x, x)
        UF.setdefault(y, y)
        UF[find(x)] = find(y)

    for w1, w2 in pairs:
        union(w1, w2)

    return all(w1 == w2 or (w1 in UF and w2 in UF and find(w1) == find(w2)) for w1, w2 in zip(words1, words2))

words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
print(areSentenceSimilarTwo(words1, words2, pairs))