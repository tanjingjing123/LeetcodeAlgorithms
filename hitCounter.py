import collections

class HitCounter:
    def __init__(self):
        self.hit_dict = collections.defaultdict(int)


    def hit(self, timestamp):
        self.hit_dict[timestamp] += 1


    def getHits(self, timestamp):
        start_time = timestamp - 300
        count = 0
        for time in self.hit_dict.keys():
            if time > start_time and time <= timestamp:
                count += self.hit_dict[time]
        return count

obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))
obj.hit(300)
print(obj.getHits(300))
print(obj.getHits(301))