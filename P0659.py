class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
		# use heap to append to current shortest subsequence
        h, hh = [], [1]
        for i in xrange(1, len(nums)):              
            if nums[i] != nums[i-1]:                
                if nums[i] == nums[i-1]+1:                    
                    if (h!=[]) and h[0] < 3: return False                    
                    h = hh                    
                else:  
                    if (hh!=[]) and hh[0] < 3: return False
                    h = []
                hh = [] 
            heapq.heappush(hh, (heapq.heappop(h) if h else 0)+1)      
        return ((h==[]) or (h[0]>=3)) and ((hh==[]) or (hh[0]>=3))