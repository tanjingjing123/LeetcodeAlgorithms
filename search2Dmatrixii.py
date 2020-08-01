class solution:

    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] > target or matrix[i][-1] < target:
                continue
            res = self.searchTarget(matrix[i], target)
            if res != -1:
                return True
        return False

    def searchTarget(self, nums, e):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < e:
                l = mid + 1
            elif nums[mid] > e:
                r = mid - 1
            else:
                return mid
        return -1

obj = solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 21
print(obj.searchMatrix(matrix, target))