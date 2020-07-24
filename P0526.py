class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """        
		# DFS for combination\permutation\subset\arrangement
        self.dp = {}
        def DFS(i, nums):         
            if i == 1: return 1
            if (i,nums) not in self.dp:
                self.dp[(i,nums)] = 0            
                for p, num in enumerate(nums):
                    if i%num == 0 or num%i == 0:
                        self.dp[(i,nums)] += DFS(i-1,nums[:p]+nums[p+1:])
            return self.dp[(i,nums)]
            
        return DFS(N, tuple(xrange(1,N+1)))