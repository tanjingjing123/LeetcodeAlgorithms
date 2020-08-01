def palindromePairs(words):
    def isPalin(string):
        for i in range(len(string) // 2):
            if (string[i] != string[-(i + 1)]):
                return False
        return True

    hashmap = {}
    for idx, word in enumerate(words):
        hashmap[word[::-1]] = idx

    res = []
    for idx, word in enumerate(words):
        l = len(word)
        for i in range(l):
            left = word[:i]
            right = word[i:]

            if left in hashmap and isPalin(right) and hashmap[left] != idx:
                res.append([idx, hashmap[left]])

                if left == "":
                    res.append([hashmap[left], idx])

            if right in hashmap and isPalin(left) and hashmap[right] != idx:
                res.append([hashmap[right], idx])
                if right == "":
                    res.append([idx, hashmap[right]])

    return res




words = ["abcd","dcba","lls","s","sssll"]
print(palindromePairs(words))