class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in s: return([s[target - nums[i]],i])
            else: s[nums[i]] = i
        return -1