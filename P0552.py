class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """    
		# 0-D DP
        A0L0, A0L1, A0L2, A1L0, A1L1, A1L2 = 1, 1, 0, 1, 0, 0     
        for _ in xrange(n):
            A0L0, A0L1, A0L2 = (A0L0 + A0L1 + A0L2)%1000000007, A0L0,  A0L1
            A1L0, A1L1, A1L2 = (A0L0 + A1L0 + A1L1 + A1L2)%1000000007, A1L0,  A1L1                                                    
        return(A1L0)