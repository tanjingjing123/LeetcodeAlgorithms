def fractionToDecimal(numerator, denominator):
    if numerator == 0:
        return "0"
    decimalPart = list()
    if ((numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0)):
        decimalPart.append('-')
    numerator = abs(numerator)
    denominator = abs(denominator)

    decimalPart.append(str(numerator // denominator))
    remainder = numerator % denominator

    if (remainder == 0):
        return ''.join(decimalPart)
    decimalPart.append('.')
    numDict = dict()
    while remainder:
        if remainder in numDict:
            decimalPart.insert(numDict[remainder], '(')
            decimalPart.append(')')
            break
        numDict[remainder] = len(decimalPart)
        remainder *= 10
        this_fraction = remainder // denominator
        decimalPart.append(str(this_fraction))
        remainder %= denominator
    return ''.join(decimalPart)

numerator = 338
denominator = 7
print(fractionToDecimal(numerator, denominator))
