class solution:
    def numSimilarGroups(self, A):
        parent = {}
        rank = {}
        def find(s):
            if parent[s] != s:
                parent[s] = find(parent[s])
            return parent[s]

        def union(s, t):
            ps = find(s)
            pt = find(t)
            if rank[ps] < rank[pt]:
                parent[ps] = pt

            else:
                parent[pt] = ps
                rank[ps] += rank[ps] == rank[pt]

        for s in A:
            parent[s] = s
            rank[s] = 0

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s = A[i]
                t = A[j]
                if self.similar(s, t):
                    union(s, t)
        return len(set(find(s) for s in A))

    def similar(self, s, t):
        return sum(a != b for a, b in zip(s, t)) <= 2


A = ["tars","rats","arts","star"]
obj = solution()
print(obj.numSimilarGroups(A))

