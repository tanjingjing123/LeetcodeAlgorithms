
def validMove(start, end):

    endState = "".join(end)
    seen = set()
    paths = []

    def checkTmp(tmp):
        if "".join(tmp) not in seen:
            seen.add("".join(tmp))
            paths.append(tmp)
            if dfs():
                return True
            seen.remove("".join(tmp))
            paths.pop()
        return False

    def dfs():
        lastPath = paths[-1]
        if "".join(lastPath) == endState:
            return True
        n = len(lastPath)
        for i, c in enumerate(lastPath):
            if c != "_":
                continue
            if i >= 1 and lastPath[i - 1] == "R":
                tmp = lastPath[::]
                tmp[i - 1] = "_"
                tmp[i] = "R"
                if checkTmp(tmp):
                    return True
            if i >= 2 and lastPath[i - 2] == "R":
                tmp = lastPath[::]
                tmp[i - 2] = "_"
                tmp[i] = "R"
                if checkTmp(tmp):
                    return True
            if i <= n - 2 and lastPath[i + 1] == "B":
                tmp = lastPath[::]
                tmp[i + 1] = "_"
                tmp[i] = "B"
                if checkTmp(tmp):
                    return True
            if i <= n - 3 and lastPath[i + 2] == "B":
                tmp = lastPath[::]
                tmp[i + 2] = "_"
                tmp[i] = "B"
                if checkTmp(tmp):
                    return True
        return False

    seen.add("".join(start))
    paths.append(start)
    dfs()

    return paths


start = ['R', '_', 'B', 'B']
end = ['B', '_', 'B', 'R']

print(validMove(start, end))
