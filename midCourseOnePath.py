import collections
def onePath(pairs):
    courses = set()
    graph = collections.defaultdict(list)
    for pair in pairs:
        courses.add(pair[0])
        courses.add(pair[1])
        graph[pair[1]].append(pair[0])

    for k in graph.keys():
        if k not in





all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "Creative Writing"],
    ["Intro to Computer Science", "Algorithms"]
]

pairs = [[1, 2], [2, 3], [3, 4], [4, 5]]