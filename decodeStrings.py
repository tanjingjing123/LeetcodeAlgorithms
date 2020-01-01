def decodeString(s):
    close_ind, stack = {}, []
    for i, c in enumerate(s):
        if c == "[":
            stack.append(i)
        elif c == "]":
            close_ind[stack.pop()] = i


    def recur(start, end):
        num = 0
        i = start
        decoded = ""

        while i <= end:
            if s[i].isalpha():
                decoded += s[i]

            elif s[i].isdigit():
                num = 10 * num + int(s[i])

            elif s[i] == '[':
                decoded += num * recur(i + 1, close_ind[i] - 1)
                num, i  = 0,  close_ind[i]
            i += 1
        return decoded

    return recur(0, len(s) - 1)


s = "21[abc]13[ced]ef"
print(decodeString(s))



