import trie
def replaceWords(dict, sentence):
    t = trie.Trie()
    for word in dict:
        t.insert(word)
    temp = sentence.split(' ')
    for i in range(len(temp)):
        p = t.commonprefix(temp[i])
        if p != -1:
            temp[i] = p
    return ' '.join(temp)

dict = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dict, sentence))
