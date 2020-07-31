class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
		# bucket sort
        N = 60*24
        bucket = [False] * N
        for s in timePoints:           
            t = int(s[:2])*60 + int(s[-2:])           
            if bucket[t]: return 0
            else: bucket[t] = True
        
        t_0 = 0
        while not bucket[t_0]: t_0 += 1
        
        tt, res = t_0, N        
        for t in range(t_0+1,N):
            if bucket[t]: res, tt = min(res, t - tt), t
                
        return(min(res, t_0 + N - tt))