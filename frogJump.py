def canCross(stones):
    if len(stones) < 2 or stones[1] != 1:
        return False
    dp = {x for x in stones}
    stack = [(1, 1)]
    visited = {(1, 1)}
    while stack:
        cur_pos, prev_k = stack.pop()
        if cur_pos == stones[-1]:
            return True
        for k in range(-1, 2):
            new_k = prev_k + k
            new_pos = cur_pos + new_k
            if new_pos > cur_pos and new_pos in dp and (new_pos, new_k) not in visited:
                visited.add((new_pos, new_k))
                stack.append((new_pos, new_k))
    return False

stones = [0,1,2,3,4,8,9,11]
print(canCross(stones))