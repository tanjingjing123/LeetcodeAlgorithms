from collections import deque


class StreamChecker:
    def __init__(self,words):
        self.tire = {}
        self.q = deque()
        self.maxqsize = 0
        for word in words:
            self.maxqsize = max(self.maxqsize, len(word))
            self.construct(word[::-1])

    def construct(self, word):
        tire = self.tire
        for ch in word:
            if ch not in tire:
                tire[ch] = {}
            tire = tire[ch]
        tire['#'] = None

    def findifexist(self, word):
        tire = self.tire
        for ch in word:
            if '#' in tire: return True
            if ch not in tire:
                break
            tire = tire[ch]
        return '#' in tire

    def query(self, letter):
        self.q.append(letter)
        if len(self.q) > self.maxqsize:
            self.q.popleft()
        if letter in self.tire:
            tocheck = list(self.q)
            tocheck.reverse()
            return self.findifexist(tocheck)
        return False

