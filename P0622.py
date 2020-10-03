class MyCircularQueue(object):
	# deque for faster front pop
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k
        self.q = collections.deque([])

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.q) == self.k:
            return False
        else:
            self.q.append(value)
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.q:
            self.q.popleft()         
            return True
        else:
            return False
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.q:
            return self.q[0]
        else:
            return -1
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.q:
            return self.q[-1]
        else:
            return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """        
        return (not self.q)
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return len(self.q) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()