import collections


class StreamChecker:
    def __init__(self, words):
        self.trie = {}
        self.suffix = collections.deque([])

        self.cap = 0
        if words:
            self.cap = max(len(w) for w in words)

        for w in words:
            cur_trie = self.trie
            for c in w[::-1]:
                if c not in cur_trie:
                    cur_trie[c] = {}
                cur_trie = cur_trie[c]
            cur_trie[None] = True

    def query(self, letter):
        if not self.cap:
            return False
        if len(self.suffix) == self.cap:
            self.suffix.pop()
        self.suffix.appendleft(letter)

        cur_trie = self.trie
        for c in self.suffix:
            if c not in cur_trie:
                return False
            cur_trie = cur_trie[c]
            if None in cur_trie:
                return True
        return False

words = ["bcd", "ef", "kkl"]
obj = StreamChecker(words)
obj.query("a")
obj.query("b")
obj.query("c")
obj.query("d")
obj.query("k")
obj.query("e")
obj.query("e")
obj.query("f")
obj.query("k")
obj.query("l")