class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        l = len(cars)
        res = [-1]*l
        s = []
        for i in range(l-1,-1,-1):            
            while s:               
                if cars[s[-1]][1] >= cars[i][1]:
                    s.pop()
                    continue                
                t = float(cars[s[-1]][0] - cars[i][0])/(cars[i][1]-cars[s[-1]][1])
                if -1 < res[s[-1]] < t:
                    s.pop()
                    continue
                res[i] = t
                break
            s.append(i)
        return res
                
            