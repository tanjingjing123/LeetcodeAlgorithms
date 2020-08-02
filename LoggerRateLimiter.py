import collections


class Logger:
    def __init__(self):
        self.memo = collections.defaultdict(int)



    def shouldPrintMessage(self, timestamp, message):
        if message not in self.memo.keys():
            self.memo[message] = timestamp
            return True
        else:
            if timestamp - self.memo[message] >= 10:
                self.memo[message] = timestamp
                return True
            else:
                return False
#["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]
# [[],[0,"A"],[ç],[0,"C"],[0,"A"],[0,"B"],[0,"C"],[11,"A"],[11,"B"],[11,"C"],[11,"A"]]

obj = Logger()
print(obj.shouldPrintMessage(0,"A"))
print(obj.shouldPrintMessage(0,"B"))
print(obj.shouldPrintMessage(0,"C"))
print(obj.shouldPrintMessage(0,"A"))
print(obj.shouldPrintMessage(0,"B"))
print(obj.shouldPrintMessage(0,"C"))
print(obj.shouldPrintMessage(11,"A"))
print(obj.shouldPrintMessage(11,"B"))
print(obj.shouldPrintMessage(11,"C"))
print(obj.shouldPrintMessage(11,"A"))
