class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """                
        l = len(startTime)  
        jobs = sorted(zip(endTime, startTime, profit))
        e = [et for et,_,_ in jobs]
        dp = [jobs[0][2]] + [0]*(l)        
        for i in range(1,l): 
            dp[i] = max(dp[i-1],dp[bisect.bisect_right(e, jobs[i][1])-1]+jobs[i][2])    
        return(dp[-2])
        
                    
        
            
        
        