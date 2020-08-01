def numberOfPatterns(m, n):
    reach_dict = {
            (1,3): 2, (1,7): 4, (1,9): 5,
            (3,1): 2, (3,7): 5, (3,9): 6,
            (7,1): 4, (7,3): 5, (7,9): 8,
            (9,1): 5, (9,3): 6, (9,7): 8,
            (4,6): 5, (6,4): 5, (2,8): 5, (8,2): 5
        }

    def backtrack(chosen):
        count = 0
        for i in range(1, 10):
            if i in chosen:
                continue

            if chosen:
                move = (chosen[-1], i)
                if move in reach_dict and reach_dict[move] not in chosen:
                    continue
            chosen.append(i)

            if len(chosen) >= m and len(chosen) <= n:
                count += 1

            if len(chosen) < n:
                count += backtrack(chosen)

            chosen.pop()
        return count
    res = backtrack([])
    return res

m = 1
n = 1
print(numberOfPatterns(m,n))
