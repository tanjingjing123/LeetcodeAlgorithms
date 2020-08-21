def reflowAndJustify(lines, maxLen):
    if not lines:
        return []

    words = []
    words.extend(lines[0].split(' '))
    for i in range(1, len(lines)):
        words.extend(lines[i].split(' '))
    result = []
    i = 0
    while i < len(words):
        remain = maxLen
        count = 0
        while i < len(words):
            if remain - len(words[i]) < 0:
                break
            count += 1
            remain -= len(words[i]) + 1
            i += 1

        line = words[i - count: i]
        n = 0
        for word in line:
            n += len(word)

        reflowed = ''
        baseDash = '-'
        if len(line) == 1:
            reflowed += line[0]
        else:
            times = (maxLen - n) // (len(line) - 1)
            extra = (maxLen - n) % (len(line)-1)

            for j in range(len(line)):
                if j == len(line) - 1:
                    reflowed += line[j]
                else:
                    if extra > 0:
                        reflowed += line[j] + baseDash * times + '-'
                        extra -= 1
                    else:
                        reflowed += line[j] + baseDash * times

        result.append(reflowed)


    return result

lines = ["The day began as still as the", "night abruptly lighted with", "brilliant flame"]
x = 24
print(reflowAndJustify(lines, x))

