import time
class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Given array is")
for i in range(len(arr)):
    print("%s" % arr[i], end=' ')
mysolution = Solution()
start_time = time.time()
mysolution.bubbleSort(arr)
end_time = time.time()
time_taken = end_time - start_time
print("\nSorted array is:")
for i in range(len(arr)):
    print("%s" % arr[i], end=' ')

print("\nthe time it takes bubble sort program:", time_taken)