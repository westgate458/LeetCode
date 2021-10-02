class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        N = len(arr)        
        if k <= N/2.0: return [arr[0],arr[-k]]        
        
        def smallerThan(m):  
            i, c, res, a, b = 0, 0, 0, -1, -1            
            for j in range(1,N):                
                while (i < N - 1) and float(arr[i])/arr[j] < m:                    
                    if float(arr[i])/arr[j] > res:
                        res, a, b = float(arr[i])/arr[j], arr[i], arr[j]                        
                    i += 1                    
                c += i            
            return c, a, b        
        l, r = 0.0, 1.0       
        while l < r:
            m = (l + r)/2
            n, a, b = smallerThan(m)  
            if n == k: break
            elif n < k: l = m
            else:  r = m
        return(a,b)