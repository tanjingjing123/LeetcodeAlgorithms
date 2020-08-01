class Solution:
    def areSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        self.parents = {}
        self.rank = {}

        for pair in pairs:
            if pair[0] not in self.parents:
                self.parents[pair[0]] = pair[0]
                self.rank[pair[0]] = 0
            if pair[1] not in self.parents:
                self.parents[pair[1]] = pair[1]
                self.rank[pair[1]] = 0

        for pair in pairs:
            self.union(pair[0], pair[1])

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words1[i] not in self.parents or words2[i] not in self.parents:
                return False
            elif self.find(words1[i]) != self.find(words2[i]):
                return False
        return True

    def find(self, word):
        if self.parents[word] != word:
            p = self.find(self.parents[self.parents[word]])
            self.parents[word] = p
        return self.parents[word]

    def union(self, w1, w2):
        p1 = self.find(w1)
        p2 = self.find(w2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parents[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parents[p1] = p2
            else:
                self.parents[p2] = p1
                self.rank[p1] += 1

myword = Solution()
words1 = ["great", "acting", "skills", "tasty"]
words2 = ["fine", "drama", "talent", "delicious"]
pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"], ["tasty", "yummy"],["yummy", "appetizing"], ["appetizing", "delicious"]]
res = myword.areSimilar(words1, words2, pairs)
print(res)
