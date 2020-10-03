class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.deque = []
        self.k = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque = [value] + self.deque
            return True
        else:
            return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque = self.deque + [value]
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if len(self.deque) > 0:            
            return self.deque[0]
        else:
            return -1

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if len(self.deque) > 0:            
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return len(self.deque) == 0    

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return len(self.deque) == self.k 


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()