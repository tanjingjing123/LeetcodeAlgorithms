import collections

class PhoneDirectory:
    def __init__(self, maxNumbers):
        self.maxNumbers = maxNumbers
        self.allNumbers = set()
        self.memo = collections.deque()
        for i in range(maxNumbers):
            self.memo.append(i)
        self.trash = set()

    def get(self):
        if self.memo:
            x = self.memo.popleft()
            self.trash.add(x)
            self.allNumbers.remove(x)
            return x
        else:
            return -1

    def check(self, number):
        if number in self.allNumbers:
            return True
        else:
            return False


    def release(self, number):
        if number in self.trash:
            self.allNumbers.add(number)
            self.memo.append(number)
            self.trash.remove()
        else:
            self.trash.add(number)
            self.memo.remove(number)

