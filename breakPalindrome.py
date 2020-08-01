def breakPalidrome(palindrome):
    if len(palindrome) < 2:
        return ""
    mid = len(palindrome) // 2
    palindrome = list(palindrome)
    has_changed = False
    for i, char in enumerate(palindrome):
        if char != 'a' and i != mid:
            palindrome[i] = 'a'
            has_changed = True
            break

    if not has_changed:
        palindrome[-1] = 'b'

    return ''.join(palindrome)

palindrome = "aaccaa"
print(breakPalidrome(palindrome))
