class solution:
    def findConcate(self, words):
        words.sort(key=len)
        if not words or not words[-1]:
            return []
        elif not words[0]:
            words = words[1:]
        wordDict = {}
        res = []
        for word in words:
            if self.valid(word, wordDict):
                res.append(word)
            tmp = wordDict
            for i in range(len(word)):
                tmp = tmp.setdefault(word[i], {})
            tmp["#"] = word
        return res

    def valid(self, word, wordDict):
        if not word:
            return True
        temp = wordDict
        for i in range(len(word)):
            if word[i] not in temp:
                return False
            temp = temp[word[i]]
            if "#" in temp and self.valid(word[i+1:], wordDict):
                return True

obj = solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(obj.findConcate(words))