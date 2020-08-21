def findRecords(records):

    for i, record in enumerate(records):
        records[i][1] = int(record[1])

    records.sort(key=lambda x: x[1])

    curMap = {}
    curEnterTime = 0
    maxP = 0
    groupSeen = {}

    for record in records:
        p = record[0]
        t = record[1]
        s = record[2]

        if s == "enter":
            curMap[p] = 1
            curEnterTime = t
        else:
            curP = list(curMap.keys())
            duration = [curEnterTime, t]

            


            del curMap[p]

    return







records = [["Paul", "1214", "enter"],
           ["Paul", "830", "enter"],
           ["Curtis", "1100", "enter"],
           ["Paul", "903", "exit"],
           ["John", "908", "exit"],
           ["Paul", "1235", "exit"],
           ["Jennifer", "900", "exit"],
           ["Curtis", "1330", "exit"],
           ["John", "815", "enter"],
           ["Jennifer", "1217", "enter"],
           ["Curtis", "745", "enter"],
           ["John", "1230", "enter"],
           ["Jennifer", "800", "enter"],
           ["John", "1235", "exit"],
           ["Curtis", "810", "exit"],
           ["Jennifer", "1240", "exit"]]


print(findRecords(records))