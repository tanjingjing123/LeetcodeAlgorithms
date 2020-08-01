import collections


class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.words = collections.defaultdict(set)

    def union(self, w1, w2):
        root1, root2 = self.find(w1), self.find(w2)

        if root1 == root2:
            return

        self.parent[root1] = root2
        self.words[root2].update(self.words[root1])
        del self.words[root1]


    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.words[x] = {x}

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

