class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
		# 0D DP, new status only depends on the one right before current one
        total, n = sum(machines), len(machines)        
        if total%n != 0: return -1
        target, acc, res = total//n, 0, 0                  
        for machine in machines:
            diff = machine - target
            acc += diff
            res = max(res,abs(acc),diff) 
        return res