import sys
from collections import defaultdict
class WordDistance:
    def __init__(self, words):
        self.pos = defaultdict(list)
        for i, word in enumerate(words):
            self.pos[word].append(i)

    def shortest(self, word1, word2):
        p1, p2 = self.pos[word1], self.pos[word2]
        i, j = 0, 0
        rst = sys.maxsize
        while i < len(p1) and j < len(p2):
            rst = min(rst, abs(p1[i] - p2[j]))
            if i == len(p1) - 1 and j == len(p2) - 1:
                return rst

            elif i == len(p1) - 1:
                j += 1
            elif j == len(p2) - 1:
                i += 1
            elif abs(p1[i+1] - p2[j]) < abs(p1[i] - p2[j+1]):
                i += 1
            else:
                j += 1

words = ["practice", "makes", "perfect", "coding", "makes", "big", "small", "coding", "makes", "coding"]
obj = WordDistance(words)
word1 = "makes"
word2 = "coding"
print(obj.shortest(word1, word2))