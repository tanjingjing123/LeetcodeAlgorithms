def groupStrings(strings):
    maps = {}
    for s in strings:
        key = []
        for i in range(len(s) - 1):
            diff = ord(s[i]) - ord(s[i+1])
            key.append(diff % 26)

        maps[tuple(key)] = maps.get(tuple(key), []) + [s]
    return maps.values()

strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(groupStrings(strings))