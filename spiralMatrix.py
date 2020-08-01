class solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        start_r, end_r, start_c, end_c = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        spiral = []
        while start_r <= end_r and start_c <= end_c:

            # Move right
            row, col = start_r, start_c
            while col <= end_c:
                spiral.append(matrix[row][col])
                col += 1
            start_r += 1

            if start_r > end_r:
                break

            # Move down
            row, col = start_r, end_c
            while row <= end_r:
                spiral.append(matrix[row][col])
                row += 1
            end_c -= 1

            if start_c > end_c:
                break

            # Move left
            row, col = end_r, end_c
            while col >= start_c:
                spiral.append(matrix[row][col])
                col -= 1
            end_r -= 1

            if start_r > end_r:
                break

            # Move up
            row, col = end_r, start_c
            while row >= start_r:
                spiral.append(matrix[row][col])
                row -= 1
            start_c += 1

            if start_c > end_c:
                break
        return spiral



matrix = [[1,2,3,4,5,6,7],[2,3,4,5,6,7,8],[3,4,5,6,7,8,9],[4,5,6,7,8,9,10]]
obj = solution()
print(obj.spiralOrder(matrix))