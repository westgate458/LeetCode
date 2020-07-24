class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
		# hash map to record previous positions with desired properties
        maps = {0:-1}
        s = res = 0        
        for p, num in enumerate(nums):
            if num == 1:
                s += 1
            else:
                s -= 1            
            if s not in maps:
                maps[s] = p 
            elif p-maps[s]>res:
                res = p-maps[s]               
        return res
                