class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        s, ans = [], [-1] * len(nums)
        for i in range(len(nums)):
            while s and nums[i] > nums[s[-1]]: ans[s.pop()] = nums[i]          
            s.append(i)
                
        for num in nums:
            while s and num > nums[s[-1]]: ans[s.pop()] = num            
            
        return ans