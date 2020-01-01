def numBoats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    res = 0
    while i <= j:
        res += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return res

people = [1, 7, 5, 6, 12, 4, 3, 9, 11]
limit = 12
print(numBoats(people, limit))