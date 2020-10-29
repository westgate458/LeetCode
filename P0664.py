class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
		# 2D DP, DFS + memorization
        s = '' .join([a for a,b in zip(s,'#'+s) if a!=b])
        d = {}
        def turn(i,j):                       
            if i>j: return 0            
            if (i,j) not in d:                
                d[(i,j)] = turn(i, j-1) + 1
                for k in range(i,j):
                    if s[k] == s[j]:
                        d[(i,j)] = min(d[(i,j)], turn(i,k)+turn(k+1,j-1))            
            return d[(i,j)]
        return turn(0,len(s)-1)
                    