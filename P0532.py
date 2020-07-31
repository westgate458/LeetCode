class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
		# hashtable for quick look-up
        if k < 0: return 0            
        d, res = set(), set()        
        for num in nums:
            if num-k in d: res.add((num-k,num)) 
            if num+k in d: res.add((num,num+k))   
            d.add(num)
        return(len(res))