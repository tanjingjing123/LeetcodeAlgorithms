
class MapSum:
    def __init__(self):
        self.trie = {}

    def insert(self, key, val):
        node = self.trie
        for c in key:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["$"] = val

    def sum(self, prefix):
        node = self.trie
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        def helper(node):
            val = node["$"] if "$" in node else 0
            return val + sum(helper(node[k]) for k in node if k != 0)
        res = helper(node)
        return res

obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))

