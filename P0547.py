class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
		# DFS for connected subgraph
        def dfs(i):
            self.v[i] = False
            for j in self.d[i]:            
                if self.v[j]: dfs(j)
        
        n = len(M)
        self.v = [True]*n
        self.d = defaultdict(set)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j] == 1:
                    self.d[i].add(j)
                    self.d[j].add(i)        
        g = 0
        for i in range(n):            
            if self.v[i]:                
                g += 1                
                dfs(i)            
        return g