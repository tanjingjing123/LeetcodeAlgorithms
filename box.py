import collections


class Valuable:
    def __init__(self, id, size):
        self._id = id
        self._size = size

    def getId(self):
        return self._id

    def getSize(self):
        return self._size


class Box:
    def __init__(self, size, valuables):
        self.idValueMap = {}
        self.sizeCountMap = collections.Counter()
        self.idSet = set()
        self.size = size
        self.curSize = 0
        for v in valuables:
            self.idValueMap[v.getId()] = v

    def add(self, valueId):
        if valueId not in self.idValueMap:
            print("Invalid id")
            return
        if valueId in self.idSet:
            print("Value already In! Don't add again!")
            return

        if self.curSize + self.idValueMap[valueId].getSize() <= self.size:
            self.sizeCountMap[self.idValueMap[valueId].getSize()] += 1
            self.idSet.add(valueId)
            self.curSize += self.idValueMap[valueId].getSize()
        else:
            print("Overload")

    def remove(self, valuable):
        if valuable.getId() in self.idSet:
            if self.sizeCountMap[valuable.getSize()] == 1:
                del self.sizeCountMap[valuable.getSize()]
            else:
                self.sizeCountMap[valuable.getSize()] -= 1

            self.idSet.remove(valuable.getId())
            self.curSize -= valuable.getSize()
        else:
            print(str(valuable.getId()) + "Not in the box")

    def getMaxSize(self):
        if not self.idSet:
            print("No values")
            return -1
        return max(self.sizeCountMap)


v1 = Valuable(1, 10)
v2 = Valuable(2, 20)
v3 = Valuable(3, 30)
v4 = Valuable(4, 40)
v5 = Valuable(5, 50)
valuables = [v1, v2, v3, v4, v5]
b = Box(100, valuables)
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.remove(v5)
b.remove(v3)
b.remove(v2)
print(b.getMaxSize())
b.remove(v4)
print(b.getMaxSize())
