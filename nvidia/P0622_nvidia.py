class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.f = -1
        self.r = -1
        self.k = k        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False                
        if self.isEmpty():
            self.f = 0           
        self.r = (self.r + 1)%self.k
        self.q[self.r] = value
        return True       

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False        
        if self.r==self.f:
            self.r = -1
            self.f = -1
        else:      
            self.f = (self.f + 1)%self.k   
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.f]        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.r]        

    def isEmpty(self) -> bool:
        return self.f==-1        

    def isFull(self) -> bool:        
        return (self.r + 1)%self.k == self.f  

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()