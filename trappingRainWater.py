from collections import deque

def trap(height):
    q = deque()
    higher_height = 0
    res = 0
    for num in height:
        if num >= higher_height:
            smaller_height, higher_height = higher_height, num
            while q:
                res += smaller_height - q.pop()
        else:
            q.append(num)
    if len(q) < 1:
        return res
    else:
        val_right = 0
        while q:
            cur_val = q.pop()
            if cur_val > val_right:
                val_right = cur_val
            else:
                res += val_right - cur_val
        return res





height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))