class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # maintain max sums of 1/2/3 windows separately, update latter results based on former ones
        win_1 = sum(nums[:k])
        win_2 = sum(nums[k:2*k])
        win_3 = sum(nums[2*k:3*k])
        
        s_1 = win_1 
        s_2 = s_1 + win_2
        s_3 = s_2 + win_3        
        
        pos_1 = [0]
        pos_2 = [0,k]
        pos_3 = [0,k,2*k]
        
        for i in range(len(nums)-3*k):          
            win_1 += nums[i+k] - nums[i]
            win_2 += nums[i+2*k] - nums[i+k]
            win_3 += nums[i+3*k] - nums[i+2*k]   
            
            if win_1 > s_1:
                s_1 = win_1
                pos_1 = [i+1]
            if win_2 + s_1 > s_2:
                s_2 = win_2 + s_1
                pos_2 = pos_1 + [i+k+1]
            if win_3 + s_2 > s_3:
                s_3 = win_3 + s_2
                pos_3 = pos_2 + [i+2*k+1] 
        return pos_3
            
                
            