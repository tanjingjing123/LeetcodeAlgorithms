def minDistance(word1, word2):
    a = len(word1)
    b = len(word2)

    matrix = [[0] * (a + 1) for _ in range(b + 1)]

    for i in range(a + 1):
        matrix[0][i] = i


    for j in range(b + 1):
        matrix[j][0] = j



    for i in range(1, b + 1):
        for j in range(1, a + 1):
            if word2[i-1] != word1[j-1]:
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
            else:
                matrix[i][j] = matrix[i-1][j-1]

    return matrix[-1][-1]

word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))