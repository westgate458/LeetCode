class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
		# choose left or right based on even\odd position
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            if m == n-1: return nums[m]
            if m%2 == 0:
                if nums[m] == nums[m+1]: l = m + 1
                else: r = m - 1
            else:
                if nums[m] == nums[m-1]: l = m + 1
                else: r = m - 1
        return nums[l]