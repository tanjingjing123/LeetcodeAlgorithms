import collections
def numOfMinutes(n, headID, manager, informTime):
    if n == 1:
        return informTime[0]

    dict = collections.defaultdict(set)
    for i in range(len(manager)):
        if manager[i] == -1:
            continue
        dict[manager[i]].add(i)

    result = [0] * n
    queue = [(0, headID)]
    while queue:
        curr_time, Id = queue.pop(0)
        if Id in dict:
            for val in dict[Id]:
                queue.append((curr_time + informTime[Id], val))
        else:
            result[Id] = curr_time

    return max(result)



n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
print(numOfMinutes(n, headID, manager, informTime))