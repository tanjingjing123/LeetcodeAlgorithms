import collections


def friendCycle2(employees, friendships):
    res = []
    friend_list = collections.defaultdict(list)
    for i in range(len(employees)):
        split_res = employees[i].split(',')
        friend_list[split_res[0]] = []


    for pair in friendships:
        pair = pair.split(',')
        x = pair[0]
        space_split = pair[1].split(' ')
        y = space_split[1]
        friend_list[x].append(y)
        friend_list[y].append(x)

    employee_department = collections.defaultdict(str)
    departments_num = collections.defaultdict(int)
    for employee in employees:
        split_res = employee.split(',')
        depart = split_res[2]
        depart_space = depart.split(' ')
        employee_department[split_res[0]] = depart_space[1]
        if depart_space[1] not in departments_num:
            departments_num[depart_space[1]] = 1
        else:
            departments_num[depart_space[1]] += 1

    info = collections.defaultdict(int)
    for dep in departments_num.keys():
        val = []
        val.append(departments_num[dep])
        info[dep] = val


    for person in friend_list.keys():
        own_dep = employee_department[person]
        for friend in friend_list[person]:
            friend_dep = employee_department[friend]
            if friend_dep != own_dep:
                update = departments_num[own_dep] - 1
                departments_num[own_dep] = update
                break

    for dep in info.keys():
        hasOther = info[dep][0] - departments_num[dep]
        info[dep].append(hasOther)


    for dep in info.keys():
        sb = ""
        sb += dep
        sb += ": "
        sb += str(info[dep][1])
        sb += " of "
        sb += str(info[dep][0])
        res.append(sb)
    return res




employees = [
    "1, Bill, Engineer",
    "2, Joe, HR",
    "3, Sally, Engineer",
    "4, Richard, Business",
    "6, Tom, Engineer"
]

friendships = [
    "1, 2",
    "1, 3",
    "3, 4"
]
print(friendCycle2(employees, friendships))
