import bisect


class Pallet:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def getId(self):
        return self.id

    def getWeight(self):
        return self.weight


class Trailer:
    def __init__(self):
        self.curWeight = 0
        self.idToObject = {}
        self.timeSlots = [0]
        self.timeWeightMap = {0: 0}

    def load(self, object, timestamp):
        self.curWeight += object.getWeight()
        self.idToObject[object.getId()] = object
        if timestamp != self.timeSlots[-1]:
            self.timeSlots.append(timestamp)
        self.timeWeightMap[timestamp] = self.curWeight

    def unload(self, id, timestamp):
        if id not in self.idToObject:
            print("No such id!")
        object = self.idToObject[id]
        self.curWeight -= object.getWeight()
        del self.idToObject[id]
        if timestamp != self.timeSlots[-1]:
            self.timeSlots.append(timestamp)
        self.timeWeightMap[timestamp] = self.curWeight

    def getTotalWeight(self, time):
        return self.search(time)

    def search(self, time):
        left = 0
        right = len(self.timeSlots)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.timeSlots[mid] > time:
                right = mid
            else:
                left = mid
        return self.timeWeightMap[self.timeSlots[left]]


p1 = Pallet(1, 2)
p2 = Pallet(2, 3)
p3 = Pallet(3, 4)
p4 = Pallet(4, 2)
p5 = Pallet(5, 5)
p6 = Pallet(6, 7)
p7 = Pallet(7, 1)
p8 = Pallet(8, 1)
p9 = Pallet(9, 3)

t = Trailer()
t.load(p1, 1)
t.load(p2, 2)
t.load(p3, 5)
t.load(p4, 7)
t.unload(p3.getId(), 7)
t.unload(p2.getId(), 8)
t.unload(p1.getId(), 9)
t.load(p5, 12)
t.load(p6, 15)
t.load(p7, 17)
t.load(p8, 18)
t.load(p9, 19)

for i in range(len(t.timeSlots)):
    print("time: " + str(t.timeSlots[i]) + " weight: " + str(t.timeWeightMap[t.timeSlots[i]]))

for i in range(20):
    print("weight at " + str(i) + " is: " + str(t.getTotalWeight(i)))
