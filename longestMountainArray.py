def longestMountain(A):
    if len(A) < 3:
        return 0
    res = 0
    cur_length = 0
    pre = A[0]
    inc = 0
    for n in A[1:]:
        if n > pre:
            if inc == 1:
                cur_length += 1
            else:
                inc = 1
                cur_length = 2
        elif n < pre:
            if inc == 1:
                inc = -1
            if inc == -1:
                cur_length += 1
                res = max(res, cur_length)
        else:
            inc = 0
        pre = n
    return res if res > 2 else 0



A = [2,1,4,7,3,2,5]
print(longestMountain(A))