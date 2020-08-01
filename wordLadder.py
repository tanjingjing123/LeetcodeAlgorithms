class Solution:

    def __init__(self):
        self.nodes = dict()

    def ladderLength(self, beginWord, endWord, wordList):
        # make a graph of nodes
        self.makeGraph([beginWord] + wordList)

        # start with the beginWord
        visited = set()
        queue = {beginWord}
        distance = 1
        while len(queue) != 0:
            nextVisit = set()
            for word in queue:
                if word == endWord:
                    return distance
                if word not in visited:
                    # add neighbors
                    for i in range(0, len(word)):
                        key = word[:i] + "*" + word[i + 1:]
                        for neighbor in self.nodes[key]:
                            nextVisit.add(neighbor)
                    visited.add(word)

            distance += 1
            queue = nextVisit
        return 0

    # nodes consist of intermediate words, with each letter replaced with "*"
    def makeGraph(self, words):
        for word in words:
            for i in range(0, len(word)):
                key = word[:i] + "*" + word[i + 1:]
                if key not in self.nodes:
                    self.nodes[key] = set()
                self.nodes[key].add(word)
obj = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(obj.ladderLength(beginWord, endWord, wordList))