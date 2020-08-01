def sequentialDigits(low, high):
    result = set()
    def helper(temp, remaining):
        if temp:
            if (low <= int(temp) <= high):
                result.add(int(temp))
            elif (int(temp) > high):
                return

        for i in range(len(remaining)):
            if (not temp or remaining[i]-int(temp[-1])==1):
                helper(temp+str(remaining[i]), remaining[i+1:])

    helper("", [i for i in range(10)])
    return (sorted(result))

low = 1000
high = 12000
print(sequentialDigits(low, high))