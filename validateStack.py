def validateStack(pushed, popped):
    stack = []
    j = 0
    i = 0
    while i < len(pushed) and j < len(popped):
        if pushed[i] == popped[j]:
            i += 1
            j += 1
        elif stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        else:
            stack.append(pushed[i])
            i += 1
    while stack and j < len(popped):
        item = stack.pop()
        if item == popped[j]:
            j += 1
        else:
            return False
    if not stack:
        return True
    else:
        return False

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStack(pushed, popped))