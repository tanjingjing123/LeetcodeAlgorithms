def longest(s):
    stack = [-1]
    res = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res, stack[-1])
    return res

s = '()()))())()'
print(longest(s))

## RC ##
## APPROACH : STACK ##
#   1. For every ‘(’ encountered, we push its index onto the stack.
#   2. For every ‘)’ encountered, we pop the topmost element and subtract the current element's index from the top element of the stack,
#      which gives the length of the currently encountered valid string of parentheses. If while popping the element, the stack becomes empty,
#      we push the current element's index onto the stack. In this way, we keep on calculating the lengths of the valid substrings, and return
#      the length of the longest valid string at the end.
