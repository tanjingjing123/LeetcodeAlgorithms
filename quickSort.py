import time
class Solution:
    def split(self, arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.split(arr, low, high)
            self.quickSort(arr, pi+1, high)

mysolution = Solution()
arr = ['S', 'O', 'R', 'T', 'I', 'N', 'G']
print("Given array is")
for i in range(len(arr)):
    print("%c" % arr[i], end=' ')
low = 0
high = len(arr) - 1
start_time = time.time()
mysolution.quickSort(arr, low, high)
end_time = time.time()
time_taken = end_time - start_time
print("\nSorted array is:")
for i in range(len(arr)):
    print("%c" % arr[i], end=' ')

print("\nthe time it takes to run this program:", time_taken)
