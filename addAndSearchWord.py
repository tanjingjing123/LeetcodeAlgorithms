class WordDictionary:
    def __init__(self):
        self.dict = {}

    def addWord(self, word):
        L = len(word)
        if L not in self.dict:
            self.dict[L] = [word]
        else:
            self.dict[L].append(word)

    def search(self, word):
        L = len(word)
        if L not in self.dict:
            return False
        for c in self.dict[L]:
            if all(i == j or j == "." for i, j in zip(c, word)):
                return True
        return False

obj =  WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search("..d"))
print(obj.search("...a"))