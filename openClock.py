import collections
def openLock(deadends, target):
    dead_set = set(deadends)
    queue = collections.deque()
    queue.append(('0000', 0))
    visited = set('0000')
    while queue:
        string, step = queue.popleft()
        if string in dead_set:
            continue
        if string == target:
            return step

        for i in range(len(string)):
            num = int(string[i])
            for dx in (-1, 1):
                num_new = (num + dx) % 10
                string_new = string[:i] + str(num_new) + string[i+1:]
                if string_new not in visited:
                    queue.append((string_new, step+1))
                    visited.add(string_new)
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(openLock(deadends, target))

