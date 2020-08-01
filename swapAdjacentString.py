def canTransform(start, end):
    nonX_start = ''.join([letter for letter in start if letter != 'X'])
    nonX_end = ''.join([letter for letter in end if letter != 'X'])

    if nonX_start == nonX_end and len(start) == len(end):
        R_start = [i for i in range(len(start)) if start[i] == 'R']
        R_end = [i for i in range(len(end)) if end[i] == 'R']
        L_start = [j for j in range(len(start)) if start[j] == 'L']
        L_end = [j for j in range(len(end)) if end[j] == 'L']
        R_not_left = all([i_start<=i_end for i_start, i_end in zip(R_start, R_end)])
        L_not_right = all([j_start>=j_end for j_start, j_end in zip(L_start, L_end)])
        if R_not_left and L_not_right:
            return True
        else:return False

    else:
        return False


start = "RXXLRXRXL"
end = "XRLXXRRLX"
print(canTransform(start, end))