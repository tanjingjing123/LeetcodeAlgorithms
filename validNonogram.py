def isValid(matrix, rowsRule, colsRule):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        cur_row = matrix[i]
        row_rule = rowsRule[i]
        row_dict = []
        consecutive_0 = 0 if matrix[i][0] else 1
        for j in range(1, len(cur_row)):
            if matrix[i][j] != 0 and consecutive_0 :
                row_dict.append(consecutive_0)
                consecutive_0 = 0
                continue
            if matrix[i][j] == 0:
                if matrix[i][j - 1] == 0:
                    consecutive_0 += 1

                if matrix[i][j - 1] == 1:
                    consecutive_0 = 1

        if consecutive_0:
            row_dict.append(consecutive_0)

        if not row_rule and not row_dict:
            continue

        for i in range(len(row_rule)):
            if row_rule[i] == row_dict[i]:
                continue
            else:
                return False

    for i in range(col):
        col_dict = []
        col_rule = colsRule[i]
        consecutive_0 = 0 if matrix[0][i] else 1
        for j in range(1, row):
            if matrix[j][i] != 0 and consecutive_0:
                col_dict.append(consecutive_0)
                consecutive_0 = 0
                continue
            if matrix[j][i] == 0:
                if matrix[j-1][i] == 0:
                    consecutive_0 += 1

                if matrix[j-1][i] == 1:
                    consecutive_0 = 1
        if consecutive_0:
            col_dict.append(consecutive_0)

        if not col_rule and not col_dict:
            continue

        for i in range(len(col_rule)):
            if col_rule[i] == col_dict[i]:
                continue
            else:
                return False
    return True


matrix1 = [[1, 1, 1, 1],
           [0, 1, 1, 1],
           [0, 1, 0, 0],
           [1, 1, 0, 1],
           [0, 0, 1, 1]]
rows1_1 = [[], [1], [1, 2], [1], [2]]
columns1_1 = [[2, 1], [1], [2], [1]]

print(isValid(matrix1, rows1_1, columns1_1))