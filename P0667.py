class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
		# smallest, largest, 2nd smallest, 2nd largest, ..., rest numbers
        res, i, j = [], 1, n        
        for kk in range(k):            
            if kk%2==0:
                res += [i]
                i += 1
            else:
                res += [j]
                j -= 1
        if k%2==1:
            return(res + range(i,j+1))
        else:
            return(res + range(j,i-1,-1))