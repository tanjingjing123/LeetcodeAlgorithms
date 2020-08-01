import time
class finalExam:
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)


        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]


        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1


        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1


        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1


    def mergeSort(self, arr, l, r):
        if l < r:

            m = (l + (r - 1)) // 2


            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)


myarr = finalExam()
arr =[8, 3, 2, 9, 7, 1, 5, 4]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=' ')
start_time = time.time()
myarr.mergeSort(arr, 0, n - 1)
end_time = time.time()
time_taken = end_time - start_time

print("\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=' ')

print("\nthe time it takes to run this program:", time_taken)