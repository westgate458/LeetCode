class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
		# 3D DP
        self.d = {}
        def dfs(i,j,k):            
            if i > j: return 0   
            if (i,j,k) not in self.d:  
                while j > i and boxes[j] == boxes[j-1]: 
                    j -= 1
                    k += 1               
                res = dfs(i,j-1,0) + (k+1)**2                
                for p in range(i,j):
                    if boxes[p] == boxes[j]: res = max(res, dfs(i,p,k+1) + dfs(p+1,j-1,0)) 
                self.d[(i,j,k)] = res
            return self.d[(i,j,k)]
        return dfs(0,len(boxes)-1,0)