class MagicDictionary:
    def __init__(self):
        self.orig_dict = {}

    def buildDict(self, dict):
        for word in dict:
            l = len(word)
            if l not in self.orig_dict:
                self.orig_dict[l] = [word]
            else:
                self.orig_dict[l].append(word)

    def search(self, word):
        def isValid(a, b):
            res = [0] * len(a)
            for idx, (i, j) in enumerate(zip(a, b)):
                if i == j:
                    res[idx] = 1
            if res.count(1) + 1 == len(a):
                return True
            return False

        l = len(word)
        if l not in self.orig_dict:
            return False
        else:
            for w in self.orig_dict[l]:
                if isValid(w, word):
                    return True
            return False

obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
print(obj.search("hello"))
print(obj.search("hhllo"))
print(obj.search("hell"))
print(obj.search("leetcoded"))