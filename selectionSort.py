
A = [8, 3, 2, 9, 7, 1, 5, 4]
print("Given array is")
for i in range(len(A)):
    print("%s" % A[i], end=' ')
for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]


print("\nSorted array")
for i in range(len(A)):
    print("%d" % A[i], end=' ')