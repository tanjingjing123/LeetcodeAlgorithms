def removeDuplicate(text):
    stack, counter, visited = [], {}, {}
    for letter in text:
        if letter not in visited:
            visited[letter] = False
            counter[letter] = 1
        else:
            counter[letter] += 1

    for letter in text:
        counter[letter] -= 1
        if visited[letter]:
            continue
        while stack and letter < stack[-1] and counter[stack[-1]] > 0:
            visited[stack[-1]] = False
            stack.pop()
        stack.append(letter)
        visited[letter] = True

    return ''.join(stack)

text = "cbacdcbc"
print(removeDuplicate(text))