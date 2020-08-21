import collections
def courseOverlap(coursePairs):
    if not coursePairs:
        return []

    memo = collections.defaultdict(list)
    for item in coursePairs:
        memo[item[0]].append(item[1])

    studentIDs = list(memo.keys())
    result = collections.defaultdict(list)
    for i in range(len(studentIDs)):
        for j in range(i+1, len(studentIDs)):
            overlaps = []
            for course1 in memo[studentIDs[i]]:
                for course2 in memo[studentIDs[j]]:
                    if course1 == course2:
                        overlaps.append(course1)
            key = '[' + str(min(studentIDs[i], studentIDs[j])) + "," + str(max(studentIDs[i], studentIDs[j])) + ']'
            result[key].append(overlaps)
    return result


coursePairs = [
    ['58', 'software design'],
    ['58', 'linear algebra'],
['94', 'art history'],
['94', 'operating systems'],
['17', 'software design'],
['58', 'mechanics'],
['58', 'economics'],
['17', 'linear algebra'],
['17', 'political science'],
['94', 'economics'],
['25', 'economics']]
print(courseOverlap(coursePairs))