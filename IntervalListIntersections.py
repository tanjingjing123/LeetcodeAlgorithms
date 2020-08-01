def intervalIntersection(A, B):
    a_ptr = b_ptr = 0
    inter_list = []
    while a_ptr < len(A) and b_ptr < len(B):
        cur_a = A[a_ptr]
        cur_b = B[b_ptr]

        low = max(cur_a[0], cur_b[0])
        high = min(cur_a[1], cur_b[1])

        if low <= high:
            inter_list.append([low, high])
        if cur_a[1] < cur_b[1]:
            a_ptr += 1
        else:
            b_ptr += 1
    return inter_list

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(A, B))