def checkvalidString(s):
    max_l = 0
    max_r = 0
    for i in range(len(s)):
        if s[i] != ')':
            max_l += 1
        else:
            max_l -= 1

        if max_l < 0:
            return False

        if s[-i-1] != '(':
            max_r += 1
        else:
            max_r -= 1

        if max_r < 0:
            return False
    return True

s = "(*(****"
print(checkvalidString(s))
