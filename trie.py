
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        temp = self.trie
        for i in range(len(word)):
            if word[i] not in temp:
                temp[word[i]] = {}
            temp = temp[word[i]]
        temp["*"] = True


    def search(self, word):
        node = self.root
        prefix = ""
        for c in word:
            if c not in node:
                return False
            ptr = node[c].root
        if 'is_end' in node:
            return prefix
        return False

    def commonprefix(self, word):
        temp = self.trie
        res = ''
        for c in word:
            if c not in temp:
                return -1
            res += c
            temp = temp[c]
            if '*' in temp:
                break
        if res == '':
            return -1
        else:
            return res

