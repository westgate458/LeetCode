class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """        
		# DPS + memorization
        self.dp = {}
        def DFS(i, j, k):
            if k == 0: return 1.0
            if (i,j,k) not in self.dp:                
                self.dp[(i,j,k)] = 0.0
                for ii, jj in [(i+1,j-2),(i+1,j+2),(i+2,j-1),(i+2,j+1),\
                               (i-1,j-2),(i-1,j+2),(i-2,j-1),(i-2,j+1)]:
                    if (0 <= ii < N) and (0 <= jj < N):                        
                        self.dp[(i,j,k)] += DFS(ii,jj,k-1)
            return(self.dp[(i,j,k)])        
        return DFS(r, c, K)/8.0**K