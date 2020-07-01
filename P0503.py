class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # use a monotonically decreasing stack
		# for each element pop previous elements that are smaller
		# current element is then the next greater element for all popped ones
		# do a second run to deal with the circular array
        s, ans = [], [-1] * len(nums)
        for i in range(len(nums)):
            while s and nums[i] > nums[s[-1]]: ans[s.pop()] = nums[i]          
            s.append(i)
                
        for num in nums:
            while s and num > nums[s[-1]]: ans[s.pop()] = num            
            
        return ans