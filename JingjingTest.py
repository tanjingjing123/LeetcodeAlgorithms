import bisect

class commodity:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def getId(self):
        return self.id

    def getWeight(self):
        return self.weight




class CyberTruck:
    def __init__(self):
        self.timeList = [0]
        self.timeWeightMap = {0:0}
        self.curWeight = 0
        self.idObjectMap = {}

    def load(self, commodity, timestamp):
        thisID = commodity.getId()
        if thisID in self.idObjectMap:
            print("Don't load again!")
            return
        self.idObjectMap[thisID] = commodity
        self.curWeight += commodity.getWeight()
        if timestamp != self.timeList[-1]:
            self.timeList.append(timestamp)
        self.timeWeightMap[timestamp] = self.curWeight


    def unload(self, id, timestamp):
        if id not in self.idObjectMap:
            print("No such id")
            return
        commodity = self.idObjectMap[id]
        self.curWeight -= commodity.getWeight()
        if timestamp != self.timeList[-1]:
            self.timeList.append(timestamp)
        self.timeWeightMap[timestamp] = self.curWeight


    def getTotalWeight(self, timestamp):
        return self.search(timestamp)


    def search(self, timestamp):
        idx = bisect.bisect_left(self.timeList, timestamp)
        return self.timeWeightMap[self.timeList[idx]]


p1 = commodity(1, 2)
p2 = commodity(2, 3)
p3 = commodity(3, 4)
p4 = commodity(4, 2)
p5 = commodity(5, 5)
p6 = commodity(6, 7)
p7 = commodity(7, 1)
p8 = commodity(8, 1)
p9 = commodity(9, 3)

t = CyberTruck()
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

for i in range(20):
    print("weight at time " + str(i) + " : " + str(t.getTotalWeight(i)))


