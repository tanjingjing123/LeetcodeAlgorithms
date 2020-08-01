def addOperators(num, target):
    def backtrack(curr, path, j):
        if j == len(num):
            if sum(curr) == target:
                paths.append(''.join(path))
            return
        for i in range(j, len(num)):
            curr_num = num[j:i+1]
            backtrack(curr + [int(curr_num)], path+["+", curr_num], i+1)
            backtrack(curr + [-int(curr_num)], path+["-", curr_num], i+1)
            backtrack(curr[:-1] + [curr[-1] * int(curr_num)], path+["*", curr_num], i+1)
            if curr_num == '0':
                return



    paths = []
    for i in range(len(num)):
        start_num = num[:i+1]
        backtrack([int(start_num)], [start_num], i + 1)
        if start_num == '0':
            break
    return paths

num = "105472"
target = 24
print(addOperators(num, target))
