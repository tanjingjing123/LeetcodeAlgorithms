import collections
def findLadders(beginWord, endWord, wordList):
    if not beginWord or not endWord or not wordList or not endWord in wordList:
        return None
    l, dic = len(endWord), collections.defaultdict(list)
    for word in wordList:
        for i in range(l):
            dic[word[:i] + "*" + word[i + 1:]].append(word)

    level = {beginWord}
    parents = collections.defaultdict(set)
    while level and endWord not in parents:
        next_level = collections.defaultdict(set)
        for node in level:
            for i in range(l):
                intermediate = node[:i] + '*' + node[i + 1:]
                for word in dic[intermediate]:
                    if word not in parents:
                        next_level[word].add(node)
        level = next_level
        parents.update(next_level)
    res = [[endWord]]
    while res and res[0][0] != beginWord:
        path = []
        for r in res:
            for p in parents[r[0]]:
                tmp = [p] + r
                path.append(tmp)
        res = path

    return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord, endWord, wordList))