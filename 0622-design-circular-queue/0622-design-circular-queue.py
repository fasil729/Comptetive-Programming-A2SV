class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.start = 0
        self.end = -1
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end =( self.end + 1) % len(self.queue)
        self.queue[self.end] = value 
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % len(self.queue)
        self.size -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.start]
        
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.end]
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == len(self.queue):
            return True
        return False

    
    
    
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()