# 622, Implementation of Circular Queue | O(1) and O(1)
class MyCircularQueue:

    def __init__(self, k: int):
        self.circ_queue = [None] * k
        self.length = k
        self.front, self.rear = -1, -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.circ_queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.length
            self.circ_queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.rear == self.front:
            self.circ_queue[self.front] = None
            self.front = self.rear = -1
        else:
            self.circ_queue[self.front] = None
            self.front = (self.front + 1) % self.length
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.circ_queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.circ_queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return ((self.rear + 1) % self.length) == self.front

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
