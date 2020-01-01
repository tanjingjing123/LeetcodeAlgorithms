def flattenDict(resultDict, myDict, parentKey):

    for key in myDict:
        if isinstance(myDict[key], dict):
            flattenDict(resultDict, myDict[key], parentKey + key)
        else:
            resultDict[parentKey + key] = myDict[key]


resultDict = {}
myDict = {"A":{"B":{"C":10, "A":33}, "D":11}, "E":12}
flattenDict(resultDict, myDict, "")
print(resultDict)