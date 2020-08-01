def camelMatch(queries, pattern):

    res = [False] * len(queries)

    def isValid(word, pattern):
        i = 0
        j = 0
        while i < len(word):
            if j < len(pattern) and word[i] == pattern[j]:
                j += 1
            elif word[i].isupper():
                return False
            i += 1
        return j == len(pattern)


    for i in range(len(queries)):
        word = queries[i]
        res[i] = isValid(word, pattern)

    return res

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"
print(camelMatch(queries, pattern))
