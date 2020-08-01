from collections import defaultdict
def wordSquares(words):
    worddict = defaultdict(list)
    for word in words:
        for i in range(1, len(word)):
            worddict[word[:i]].append(word)

    def search(worddict, ans, index, res):
        if index == len(word):
            return res.append(ans)
        prefix = ""
        for entry in ans:
            prefix += entry[index]

        for option in worddict[prefix]:
            search(worddict, ans + [option], index + 1, res)

    res = []
    for word in words:
        ans = [word]
        search(worddict, ans, 1, res)
    return res

words = ["abat","baba","atan","atal"]
print(wordSquares(words))