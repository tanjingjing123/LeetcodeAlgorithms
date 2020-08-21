class solution:
    def spiralOrder(self, matrix):
        right = 0
        down = 1
        left = 2
        up = 3

        direction = 0
        spiral = []
        while len(matrix):
            if direction == right:
                spiral += matrix[0]
                matrix = matrix[1:]
            elif direction == down:
                matrix = list(zip(*matrix))
                spiral += matrix[-1]
                matrix = list(zip(*matrix[:-1]))
            elif direction == left:
                spiral += reversed(matrix[-1])
                matrix = matrix[:-1]
            elif direction == up:
                matrix = list(zip(*matrix))
                spiral += reversed(matrix[0])
                matrix = list(zip(*matrix[1:]))
            direction = (direction + 1) % 4
        return spiral



matrix = [[1,2,3,4,5,6,7],[2,3,4,5,6,7,8],[3,4,5,6,7,8,9],[4,5,6,7,8,9,10]]
obj = solution()
print(obj.spiralOrder(matrix))