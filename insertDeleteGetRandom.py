import random


class randomizedSet:
    def __init__(self):
        self.dict = set()


    def insert(self, val):
        if val not in self.dict:
            self.dict.add(val)
            return True
        return False

    def remove(self, val):
        if val in self.dict:
            self.dict.remove(val)
            return True
        return False


    def getRandom(self):
        tmp = list(self.dict)
        return tmp[random.randint(0, len(tmp) - 1)]

obj = randomizedSet()
obj.insert(3)
obj.insert(3)
obj.insert(1)
obj.insert(4)
obj.insert(5)
obj.insert(2)
obj.insert(2)
print(obj.getRandom())