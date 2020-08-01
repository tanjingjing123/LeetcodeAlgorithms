def minDominoRotations(A, B):
    def min_rotate_to_target(target, A, B):
        rotate_count_A = 0
        rotate_count_B = 0

        for i in range(len(A)):
            if A[i] != target and B[i] != target:
                return float("inf")

            if A[i] != target:
                rotate_count_A += 1

            if B[i] != target:
                rotate_count_B += 1
        return min(rotate_count_A, rotate_count_B)


    min_rotate_to_A0 = min_rotate_to_target(A[0], A, B)
    min_rotate_to_B0 = min_rotate_to_target(B[0], A, B)

    result = min(min_rotate_to_A0, min_rotate_to_B0)

    if result == float("inf"):
        return -1
    return result

A = [1,2,2,4,2,2]
B = [2,5,6,2,3,2]

print(minDominoRotations(A, B))
