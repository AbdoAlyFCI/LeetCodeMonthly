# 622. Design Circular Queue (Medium)
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None]*k
        self.count = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if len(self.arr) == self.count:
            return False

        self.rear += 1

        if self.rear == len(self.arr):
            self.rear = 0

        self.arr[self.rear] = value
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        
        self.arr[self.front] = None
        self.front +=1
        
        if self.front == len(self.arr):
            self.front = 0

        self.count -=1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1

        return self.arr[self.front]

    def Rear(self) -> int:
        if self.count == 0:
            return -1

        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == len(self.arr) else False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_2 = obj.enQueue(2)
param_3 = obj.enQueue(3)
param_4 = obj.enQueue(4)
param_5 = obj.Rear()
param_6 = obj.isFull()
param_7 = obj.deQueue()
param_8 = obj.enQueue(4)
param_9 = obj.Rear()
