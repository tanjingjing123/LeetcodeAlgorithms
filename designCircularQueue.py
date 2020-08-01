class MyCircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.start = 0
        self.end = 0
        self.counter = 0
        self.size = k


    def enQueue(self, value):
        if (not self.isFull()):
            self.queue[self.end] = value
            self.end += 1
            self.counter += 1

            if (self.end == self.size):
                self.end = 0

            return True

        else:
            return False

    def deQueue(self):
        if (not self.isEmpty()):
            self.start += 1
            self.counter -= 1

            if (self.start == self.size):
                self.start = 0

            return True
        else:
            return False


    def Front(self):
        if (not self.isEmpty()):
            return self.queue[self.start]
        else:
            return -1


    def Rear(self):
        if (not self.isEmpty()):
            index = self.end - 1 if self.end != 0 else self.size - 1
            return self.queue[index]
        else:
            return -1


    def isEmpty(self):
        if self.counter == 0:
            return True
        else:
            return False


    def isFull(self):
        if self.counter == self.size:
            return True
        else:
            return False


