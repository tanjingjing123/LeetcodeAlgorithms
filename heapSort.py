import time
class Solution:
    def makeHeap(self, arr, n, i):
        maxNum = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            maxNum = left

        if right < n and arr[maxNum] < arr[right]:
            maxNum = right

        if maxNum != i:
            arr[i], arr[maxNum] = arr[maxNum],arr[i]
            self.makeHeap(arr, n, maxNum)

    def heapSort(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.makeHeap(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.makeHeap(arr, i, 0)

mysolution = Solution()
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Given array is")
for i in range(len(arr)):
    print("%s" % arr[i], end=' ')

start_time = time.time()
mysolution.heapSort(arr)
end_time = time.time()
time_taken = end_time - start_time
print("\nSorted array is:")
for i in range(len(arr)):
    print("%s" % arr[i], end=' ')

print("\nthe time it takes to run this program:", time_taken)

