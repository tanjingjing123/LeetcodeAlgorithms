def checkInclusion(s1, s2):
    s, e = 0, len(s1)
    s1 = sorted(s1)
    chars = list(set(s1))
    while s <= len(s2) - e:
        if s2[s] in chars and sorted(s2[s:s+e]) == s1:
            return True
        s += 1
    return False

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))