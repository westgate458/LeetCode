class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m, n = len(points), len(points[0])        
        res = [[0] *n for _ in range(m)]        
        res[0] = points[0]        
        for i in range(1,m):
            res_left = -float('inf')
            for j in range(n):
                res_left = max(res_left, res[i-1][j]+j)
                res[i][j] = max(res[i][j], res_left-j+points[i][j])
            res_right = -float('inf')
            for j in range(n-1,-1,-1):
                res_right = max(res_right, res[i-1][j]-j)
                res[i][j] = max(res[i][j], res_right+j+points[i][j])                     
        return max(res[-1])