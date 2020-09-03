class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """      
		# DFS + memorization
        d = {}
        def DFS(N, i, j):   
            if (i < 0) or (j < 0) or (i >= m) or (j >= n): return 1
            elif (N == 0): return 0
            elif (N,i,j) not in d: d[(N,i,j)] = (DFS(N-1, i-1, j)+DFS(N-1, i, j-1)+DFS(N-1, i+1, j)+DFS(N-1, i, j+1))%1000000007
            return d[(N,i,j)]        
        return DFS(N, i, j)
            
            
        
            