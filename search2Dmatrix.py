def searchMatrix(matrix, target):
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    left = 0
    right = len(matrix) - 1
    search_row = None

    while left <= right:
        mid = left + (right - left) // 2

        if matrix[mid][0] <= target <= matrix[mid][-1]:
            search_row = mid
            break
        if matrix[mid][-1] < target:
            left = mid + 1
            continue
        if matrix[mid][0] > target:
            right = mid - 1
            continue

    if search_row == None:
        return False

    left = 0
    right = len(matrix[search_row]) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if matrix[search_row][mid] == target:
            return True
        if target < matrix[search_row][mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 30
print()