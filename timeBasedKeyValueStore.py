import bisect
import collections

class TimeMap:
    def __init__(self):
        self.memoOfValue = collections.defaultdict(list)
        self.memoOfTimestamp = collections.defaultdict(list)


    def set(self, key, value, timestamp):
        self.memoOfValue[key].append(value)
        self.memoOfTimestamp[key].append(timestamp)

    def get(self, key, timestamp):
        idx = bisect.bisect_right(self.memoOfTimestamp[key], timestamp)
        if idx == 0:
            return ""
        else:
            return self.memoOfValue[key][idx - 1]



obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo",  1))
print(obj.get("foo",  3))
obj.set("foo", "bar2", 4)
print(obj.get("foo",  4))
print(obj.get("foo",  5))
obj.set("foo", "bar3", 7)
print(obj.get("foo",  6))
obj.set("foo", "bar4", 11)
print(obj.get("foo",  15))

