from random import random
class solution:
    def findSecret(self, wordlist, master):
        dist = lambda s1, s2: sum([1 for c1, c2 in zip(s1, s2) if c1 == c2])
        seen = set(wordlist)
        score = 0
        for i in range(10):
            choice = seen.pop() if seen else ""
            score = master.guess(choice)
            seen = {w for w in seen if dist(choice. w) == score}


