from functools import cmp_to_key
def sortRoman(names):
    def convertToNum(roman):
        romanMap = {"I": 1, "V": 5, "X":10, "L": 50}
        value = 0
        for i in range(len(roman)):
            if i > 0 and romanMap[roman[i]] > romanMap[roman[i - 1]]:
                value += romanMap[roman[i]] - 2 * romanMap[roman[i-1]]
            else:
                value += romanMap[roman[i]]
        return value

    def comparator(x, y):
        xData = x.split(' ')
        yData = y.split(' ')
        if xData[0] != yData[0]:
            return -1 if xData[0] < yData[0] else 1
        return convertToNum(xData[1]) - convertToNum(yData[1])

    return sorted(names, key=cmp_to_key(comparator))


names = ["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XX", "Steven XVI"]
print(sortRoman(names))