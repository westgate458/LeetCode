class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def DFS(kk, nums, s, j):
            if (kk == k) and (not nums): return True            
            for i in range(j,len(nums)):
                if s+nums[i] < target:
                    if DFS(kk, nums[:i]+nums[i+1:], s+nums[i], i): return True
                elif s+nums[i] == target:
                    if DFS(kk+1, nums[:i]+nums[i+1:], 0, 0): return True                    
            return False
        
        if k > len(nums): return False        
        sums = sum(nums)
        if sums % k != 0: return False        
        target = sums/k        
        nums.sort(reverse=True)
        if nums[0] > target: return False
        return DFS(0, nums, 0, 0)