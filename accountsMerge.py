import collections


def accountsMerge(accounts):
    parent = dict()

    def add(x):
        if x not in parent:
            parent[x] = x

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parentX = find(x)
        parentY = find(y)
        if parentX != parentY:
            parent[parentY] = parentX

    email_to_name_hashmap = dict()
    for account in accounts:
        name = account[0]
        emails = account[1:]
        email_to_name_hashmap[emails[0]] = name
        add(emails[0])
        for i in range(1, len(emails)):
            email_to_name_hashmap[emails[i]] = name
            add(emails[i])
            add(emails[i - 1])
            union(emails[i - 1], emails[i])

    # print parent
    res = collections.defaultdict(list)
    for email in parent:
        x = find(email)
        res[x].append(email)

    ans = []
    for key in res:
        val = []
        val.append(email_to_name_hashmap[key])
        val.extend(sorted(res[key]))
        ans.append(val)
    return ans

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(accountsMerge(accounts))