import bisect
def findClosestElements(arr, k, x):
    idx = bisect.bisect(arr, x)
    lidx = ridx = idx

    while lidx >= 0 and ridx < len(arr):
        if ridx - lidx + 1 > k:
            if abs(arr[lidx] - x) <= abs(arr[ridx] - x):
                return arr[lidx:lidx + k]

            else:
                return arr[lidx+1:lidx+k+1]

        if abs(arr[lidx] - x) <= abs(arr[ridx] - x):
            lidx -= 1
        else:
            ridx += 1

    return arr[ridx-k:ridx] if lidx >= 0 else arr[lidx+1:lidx+k+1]
arr = [1,2,3,4,5,6,7,8]
x = 4
k = 5
print(findClosestElements(arr, k, x))