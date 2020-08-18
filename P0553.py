class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """       
		# alternative to DFS 		
        return('/'.join([str(num) for num in nums]) if len(nums) <= 2 else str(nums[0]) + '/(' + '/'.join([str(num) for num in nums[1:]]) + ')')