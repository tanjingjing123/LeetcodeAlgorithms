class DisjointSet(object):
    def __init__(self):
        self.parent = {}
        self.val = {}

    def add(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.val[node] = 1

    def union(self, node_a, node_b, l):
        root_a, val_a = self.find(node_a)
        root_b, val_b = self.find(node_b)

        if root_a != root_b:
            self.parent[root_a] = root_b
            self.val[root_a] = l * val_b / val_a

    def find(self, node):
        if node not in self.parent: return None, None
        if self.parent[node] == node: return node, 1

        root, parent_root_val = self.find(self.parent[node])

        self.parent[node] = root
        self.val[node] *= parent_root_val

        return self.parent[node], self.val[node]


class Solution:
    def calcEquation(self, equations, values, queries):
        disjoint_set = DisjointSet()

        for i in range(len(equations)):
            u, v = equations[i]
            l = values[i]

            disjoint_set.add(u)
            disjoint_set.add(v)
            disjoint_set.union(u, v, l)

        result = []
        for u, v in queries:
            root_u, val_u = disjoint_set.find(u)
            root_v, val_v = disjoint_set.find(v)

            if not root_u or not root_v or root_u != root_v:
                result.append(-1)
                continue

            result.append(val_u / val_v)

        return result
obj = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(obj.calcEquation(equations, values, queries))