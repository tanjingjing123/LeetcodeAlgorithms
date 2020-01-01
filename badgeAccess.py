def invalidBadgeRecords(records):
    if not records:
        return []

    result = [[], []]
    state = {}
    invalidEnter = set()
    invalidExit = set()
    for record in records:
        if record[0] not in state:
            state[record[0]] = 0
        if record[1] == 'enter':
            if state[record[0]] == 0:
                state[record[0]] = 1
            else:
                invalidEnter.add(record[0])
        else:
            if state[record[0]] == 1:
                state[record[0]] = 0
            else:
                invalidExit.add(record[0])

    for k, v in state.items():
        if v == 1:
            invalidEnter.add(k)


    for name in invalidEnter:
        result[0].append(name)

    for name in invalidExit:
        result[1].append(name)

    return result

badge_records = [["Martha","exit"],["Paul","enter"],["Martha","enter"],["Martha","exit"],["Jennifer", "enter"],
                 ["Paul", "enter"],["Curtis", "enter"],["Paul","exit"],["Martha",   "enter"],["Martha",   "exit"],
                 ["Jennifer", "exit"]]
print(invalidBadgeRecords(badge_records))
