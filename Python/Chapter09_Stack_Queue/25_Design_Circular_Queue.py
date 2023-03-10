# 622. Design Circular Queue

class MyCircularQueue:
    
    def __init__(self, k: int):
        self.stack = [None] * k
        self.max = k
        self.size = 0
        self.front = 0
        self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        if self.size == self.max:
            return False
        self.rear = (self.rear + 1) % self.max
        self.stack[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.stack[self.front] = None
        self.front = (self.front + 1) % self.max
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.stack[self.front] == None:
            return -1
        else:
            return self.stack[self.front]

    def Rear(self) -> int:
        if self.stack[self.rear] == None:
            return -1;
        else:
            return self.stack[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()