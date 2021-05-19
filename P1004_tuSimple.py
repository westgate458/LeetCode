class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l_max = l = n_zeros = 0        
        for r, num in enumerate(nums):            
            if num == 0:
                n_zeros += 1
                while (n_zeros > k) and (l <= r):                    
                    if nums[l] == 0:
                        n_zeros -= 1
                    l += 1            
            l_max = max(l_max, r - l + 1) 
        return(l_max)