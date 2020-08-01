def minFlipsMonoIncr(S):
    flip0 = 0
    flip1 = 0
    for i in range(len(S)):
        if S[i] == "0":
            flip1 = min(flip0, flip1) + 1
        else:
            flip1 = min(flip0, flip1)
            flip0 = flip0 + 1

    return min(flip0, flip1)

S = "010110"
print(minFlipsMonoIncr(S))