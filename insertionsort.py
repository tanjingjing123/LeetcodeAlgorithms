def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Given array is")
for i in range(len(A)):
    print("%s" % A[i], end=' ')
insertionSort(A)
print("\nSorted array")
for i in range(len(A)):
    print("%d" % A[i], end=' ')