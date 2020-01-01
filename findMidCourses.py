import collections
def findMidCourses(pairs):
    graph = collections.defaultdict(list)
    parent = collections.defaultdict(int)
    for pair in pairs:
        graph[pair[0]].append(pair[1])
        parent[pair[1]] += 1

    result = set()

    memo = collections.defaultdict(list)
    def rec(curNode, preCount):
        if curNode in memo:
            return memo[curNode]

        counts = set()
        if not graph[curNode]:
            counts.add(0)
        else:
            for child in graph[curNode]:
                counts.update(rec(child, preCount + 1))

        curCount = []
        for count in counts:
            if preCount == count or preCount == count - 1:
                result.add(curNode)
            curCount.append(count + 1)


        memo[curNode] = curCount
        return curCount

    for pair in pairs:
        if pair[0] not in parent:
            rec(pair[0], 0)

    return result

pairs = [["Logic", "COBOL"], ["Data Structures", "Algorithms"], ["Creative Writing", "Data Structures"], ["Algorithms", "COBOL"],
         ["Intro to Computer Science", "Data Structures"], ["Logic", "Compilers"], ["Data Structures", "Logic"],
         ["Creative Writing", "System Administration"], ["Databases", "System Administration"], ["Creative Writing", "Databases"],
         ["Intro to Computer Science", "Graphics"]]
print(findMidCourses(pairs))

