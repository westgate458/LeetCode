class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
		# start from each character and expand in both ways, stop when mismatch found
        l, res = len(s), 0        
        for m in range(2*l-1):              
            i, j = m//2, m//2+m%2   
            while (i>=0) and (j<l) and s[i] == s[j]:
                res, i, j = res+1, i-1, j+1                
        return(res)