class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
		# check for loops one by one		
        v, res, l = [True] * len(nums), 0, 0
        for i in range(len(nums)):                      
            while v[i]:
                v[i], i, l = False, nums[i], l+1   
            if l > res: res = l
            l = 0
        return res