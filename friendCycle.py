import collections


def friendCycle(employees, friendships):
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

    for person in friend_list.keys():
        ones_friends = ""
        ones_friends += person
        ones_friends += ": "
        if len(friend_list[person]) != 0:
            ones_friends += str(friend_list[person])
        else:
            ones_friends += "None"
        res.append(ones_friends)
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

print(friendCycle(employees, friendships))