class solution:
    def detectCapitalUse(self, word):
        if len(word) == 1:
            return True
        first = ord(word[0])
        second = ord(word[1])
        if (first >= 65 and first <= 90):
            if (second >= 65 and second <= 90):
                for ch in word[2:]:
                    if ord(ch) < 65 or ord(ch) > 90:
                        return False
                    else:continue
            else:
                for ch in word[2:]:
                    if ord(ch) >= 65 and ord(ch) <= 90:
                        return False
                    else:
                        continue
        else:
            for ch in word[1:]:
                if ord(ch) >= 65 and ord(ch) <= 90:
                    return False
                else:
                    continue

        return True


obj = solution()
print(obj.detectCapitalUse("FlaG"))
print(obj.detectCapitalUse("USA"))
print(obj.detectCapitalUse("china"))
print(obj.detectCapitalUse("flaGa"))
print(obj.detectCapitalUse("Flag"))