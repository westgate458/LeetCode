class Logger(object):

    def __init__(self):
        self.d = defaultdict(int)

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        res = False
        if timestamp - self.d.get(message,-10) >= 10:           
            res = True
            self.d[message] = timestamp
        return res
                
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)