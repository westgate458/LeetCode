class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
		# form permutations of nums, then try all possible operations between each two numbers
        def check(n,i):
            return any([DFS(n[:i]+[n[i]+n[i+1]]+n[i+2:]),DFS(n[:i]+[n[i]-n[i+1]]+n[i+2:]),DFS(n[:i]+[n[i]*n[i+1]]+n[i+2:]),(n[i+1]!=0 and DFS(n[:i]+[n[i]/n[i+1]]+n[i+2:]))])
        def DFS(n):            
            if len(n) == 1: return(23.9<=n[0]<=24.1)                            
            else: return any([check(n,i) for i in range(len(n)-1)]) 
        return any(DFS(list(xs)) for xs in set(itertools.permutations([float(n) for n in nums])))