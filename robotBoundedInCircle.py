class solution:
    def __init__(self):
        self.directions = {0:'N', 1:'E', 2:'S', 3:'W'}
    def isRobotBounded(self, instructions):
        curr = [0, 0]
        direction = 0
        for move in instructions:
            if move == 'G':
                curr = self.move(curr, direction)
            else:
                direction = self.turn(move, direction)
        if curr == [0, 0] or direction != 0:
            return True
        else:
            return False


    def move(self, start, direction):
        if direction == 0:
            start[1] += 1
        elif direction == 1:
            start[0] += 1
        elif direction == 2:
            start[1] -= 1
        else:
            start[0] -= 1
        return start

    def turn(self, move, direction):
        if move == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        return direction

obj = solution()
instructions = "GLLRRGGLRGGRGG"
print(obj.isRobotBounded(instructions))