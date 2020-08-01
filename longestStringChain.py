def longestStrChain(words):
    prevs = {}

    for w in sorted(words, key=lambda x:len(x)):
        prevs[w] = 1
        for i in range(len(w)):
            prev = w[:i] + w[i+1:]
            if prev in prevs:
                prevs[w] = max(prevs[w], prevs[prev] + 1)
    return max(prevs.values())


words = ["a","b","ba","bca","bda","bdca", "bccdaa"]
print(longestStrChain(words))