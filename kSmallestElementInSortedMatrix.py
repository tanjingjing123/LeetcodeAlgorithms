class Solution:
    def kthSmallest(self, matrix, k):
        row = len(matrix)
        col = len(matrix[0])
        left, right = matrix[0][0], matrix[row - 1][col - 1]

        while left < right:
            mid = (left + right) // 2
            count = self.findNotBiggerThanMid(matrix, mid, row, col)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return right

    # count the number of elements which smaller than or equal to mid from the lower left corner of the matrix
    def findNotBiggerThanMid(self, matrix, mid, row, col):
        i, j, count = row - 1, 0, 0
        while i >= 0 and j < col:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count
obj = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(obj.kthSmallest(matrix, k))