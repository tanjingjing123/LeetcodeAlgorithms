import collections

def largestGroup(records):
    for i in range(len(records)):
        records[i][1] = int(records[i][1])

    records.sort(key = lambda x: x[1])

    groupMap = collections.defaultdict(list)
    curGroup = set()

    def subsets(candidates):
        res = [[]]
        for i in range(len(candidates)):
            tmp = res[::]
            for seq in tmp:
                res.append(seq + [candidates[i]])
        return res

    for record in records:
        if record[2] == "enter":
            combList = subsets(list(curGroup))
            for comb in combList:
                comb.append(record[0])
                comb.sort()
                groupMap[",".join(comb)].append(record[1])
            curGroup.add(record[0])
        else:
            curGroup.remove(record[0])
            combList = subsets(list(curGroup))
            for comb in combList:
                comb.append(record[0])
                comb.sort()
                groupMap[",".join(comb)].append(record[1])
    maxOccur = None
    for key, values in groupMap.items():
        if maxOccur is None or (len(values) >= 4 and len(maxOccur[0].split(",")) < len(key.split(","))):
            maxOccur = [key, values]
    if not maxOccur:
        print("None group found")
    else:
        resultStr = maxOccur[0] + ": "

        for i in range(len(maxOccur[1]) // 2):
            resultStr += str(maxOccur[1][i * 2]) + " to " + str(maxOccur[1][i * 2 + 1])
            if i < (len(maxOccur[1]) // 2 - 1):
                resultStr += ", "
        print(resultStr)


records = [
  ["Paul",     "1214", "enter"],
  ["Paul",      "830", "enter"],
  ["Curtis",   "1100", "enter"],
  ["Paul",      "903", "exit"],
  ["John",      "908", "exit"],
  ["Paul",     "1235", "exit"],
  ["Jennifer",  "900", "exit"],
  ["Curtis",   "1330", "exit"],
  ["John",      "815", "enter"],
  ["Jennifer", "1217", "enter"],
  ["Curtis",    "745", "enter"],
  ["John",     "1230", "enter"],
  ["Jennifer",  "800", "enter"],
  ["John",     "1235", "exit"],
  ["Curtis",    "810", "exit"],
  ["Jennifer", "1240", "exit"],
]
largestGroup(records)