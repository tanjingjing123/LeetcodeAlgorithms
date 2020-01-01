def minScore(lines):
    raw_total = 0
    total_words = 0
    for line in lines:
        line = line.split(' ')
        for word in line:
            raw_total += len(word) + 1
            total_words += 1

    words = []
    words.extend(lines[0].split(' '))
    for i in range(1, len(lines)):
        words.extend(lines[i].split(' '))
    def getScore(words, lengthPerLine):




    min_score = 0
    for k in range(2, total_words+1):
        lengthPerLine = raw_total // k
        cur_score = getScore(lines, lengthPerLine, k)
        min_score = min(cur_score, min_score)

    return min_score







lines = ["The day began as still as the", "night abruptly lighted with", "brilliant flame"]
print(minScore(lines))