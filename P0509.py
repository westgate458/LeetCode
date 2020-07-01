class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
		# 0-D DP
        f = [0,1] + [0] * N        
        for n in range(2,N+1): f[n] = f[n-1]+f[n-2] 
        return f[N]