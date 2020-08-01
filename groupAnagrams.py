def groupAnagrams(strs):
    h = {}
    for word in strs:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in h:
            h[sortedWord] = [word]
        else:
            h[sortedWord].append(word)

    final = []
    for value in h.values():
        final.append(value)

    return final

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))