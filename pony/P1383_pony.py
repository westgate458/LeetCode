class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()        
        j = 0
        for i in range(len(nums)):
            k += nums[i]
            if k < (i-j+1)*nums[i]:
                k -= nums[j]
                j += 1            
        return(i-j+1)