def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split()
    stack = []
    for word in words:
        word = list(word)
        for i, ch in enumerate(word):
            if ord(ch) >= 65 and ord(ch) <= 90:
                word[i] = ch.lower()
            else:
                word[i] = ch.upper()
        word = ''.join(word)
        stack.append(word)
    res = []
    while stack:
        word = stack.pop()
        res.append(word)
    return res


sentence = "aWESOME is cODING"
print(reverse_words_order_and_swap_cases(sentence))