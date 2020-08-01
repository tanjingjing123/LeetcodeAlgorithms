class solution:
    def cleanRoom(self, robot):
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = []
        def keepgoing(row, col, direct):
            visited.append((row, col))
            robot.clean()
            for k in range(4):
                new_d = (k + direct) % 4
                new_r = row + direction[new_d][0]
                new_c = col + direction[new_d][1]

                if (new_r, new_c) not in visited and robot.move():
                    keepgoing(new_r, new_c, new_d)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()
        keepgoing(0, 0, 0)