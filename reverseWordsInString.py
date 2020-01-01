def reverseWords(s):
    spacesArray = []
    i = 0
    while i < len(s):
        countSpaces = 0
        while i < len(s) and s[i] == " ":
            countSpaces += 1
            i += 1
        if countSpaces != 0: spacesArray.append(countSpaces)
        i += 1
    chars = [t for t in s]
    slow, n = 0, len(s)
    for fast in range(n):
        if chars[fast] != ' ' or (fast > 0 and chars[fast] == ' ' and chars[fast-1] != ' '):
            chars[slow] = chars[fast]
            slow += 1

    if slow == 0:
        return ''

    chars = chars[:slow-1] if chars[-1] == ' ' else chars[:slow]
    chars.reverse()
    slow, m = 0, len(chars)
    for fast in range(m + 1):
        if fast == m or chars[fast] == ' ':
            chars[slow:fast] = chars[slow:fast][::-1]
            slow = fast + 1
    print(''.join(chars))
    return ''.join(chars)
s = "hello world! a      good        example  "
print(reverseWords(s))