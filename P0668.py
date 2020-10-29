class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """ 
		# count numbers smaller than mid in each row
        l, r = 1, m*n              
        while l < r:
            mid, count = (l+r)//2, 0            
            for row in range(1, m+1):
                if mid >= row*n:
                    count += n
                elif mid < row:
                    break
                else:                    
                    count += mid//row            
            if count < k:
                l = mid + 1
            else:
                r = mid        
        return(l)
        