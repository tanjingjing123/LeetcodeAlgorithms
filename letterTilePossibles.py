import collections


class solution:
    ans = 0
    def numTilePossible(self, tiles):
        counter = collections.Counter(tiles)
        for i in range(1, len(tiles) + 1):
            self.words(i, counter, '')
        return self.ans

    def words(self, length, counter, word):
        if length == len(word):
            self.ans += 1
            return

        for k, v in counter.items():
            if v > 0:
                counter[k] -= 1
                self.words(length, counter, word + k)
                counter[k] += 1

obj = solution()
tiles = "AABB"
print(obj.numTilePossible(tiles))
