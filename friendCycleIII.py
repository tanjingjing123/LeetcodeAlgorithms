
def isCycle(employees, friendships):
    persons = set()
    for employee in employees:
        employee = employee.split(',')
        person = int(employee[0])
        persons.add(person)

    parent_dict = {i: i for i in persons}
    def find(x):
        parent = parent_dict[x]
        if parent != x:
            parent_dict[x] = find(parent_dict[x])
        return parent_dict[x]

    def union(x, y):
        parentX = find(x)
        parentY = find(y)
        if parentX != parentY:
            parent_dict[parentY] = parentX


    for pair in friendships:
        pair = pair.split(',')
        x = int(pair[0])
        space_split = pair[1].split(' ')
        y = int(space_split[1])
        union(x, y)

    res_set = set()
    for v in parent_dict.values():
        res_set.add(v)

    return len(res_set) == 1


employees = [
    "1, Bill, Engineer",
    "2, Joe, HR",
    "3, Sally, Engineer",
    "4, Richard, Business",
    "6, Tom, Engineer",
    "8, Amy, Engineer",
    "12, Jane, Engineer"
]

friendships = [
    "1, 2",
    "1, 3",
    "3, 4",
    "4, 12"
]
print(isCycle(employees, friendships))