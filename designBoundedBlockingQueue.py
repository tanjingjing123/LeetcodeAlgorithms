from threading import Semaphore


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.e = Semaphore(capacity)
        self.d = Semaphore(0)
        self.q = []

    def enqueue(self, element: int) -> None:
        self.e.acquire()
        self.q.append(element)
        self.d.release()

    def dequeue(self) -> int:
        self.d.acquire()
        element = self.q.pop(0)
        self.e.release()
        return element

    def size(self) -> int:
        return len(self.q)

obj = BoundedBlockingQueue(3)
obj.enqueue(1)
obj.enqueue(0)
obj.enqueue(2)
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
obj.enqueue(2)
print(obj.size())
print(obj.dequeue())
