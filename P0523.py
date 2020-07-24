class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """   
        # hash map to record previous positions with desired properties
        mod, mod_pos = 0, {0:-1}
        
        for idx, num in enumerate(nums):
            mod += num
            if k != 0: mod %= k
            if mod in mod_pos:
                if idx-mod_pos[mod]>1: return True
            else:
                mod_pos[mod] = idx
            
        return False
            