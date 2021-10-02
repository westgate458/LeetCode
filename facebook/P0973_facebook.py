class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """        
        h = [(-1e9,-1)]*k 
        for p in points:
            dp = p[0]**2+p[1]**2
            if dp < -h[0][0]:
                heapq.heapreplace(h, (-dp, p)) 
        return([x[1] for x in h])