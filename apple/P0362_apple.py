class HitCounter(object):

    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        if (not self.hits) or (self.hits[-1][0]<timestamp):
            self.hits.append([timestamp,1])
        else:
            self.hits[-1][1] += 1        

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        r = 0
        for hit in self.hits[::-1]:
            if hit[0] > timestamp-300:
                r += hit[1]
            else:
                break       
        return(r)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)