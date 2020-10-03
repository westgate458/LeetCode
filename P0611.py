class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		# 3Sum: fix largest and find ranges for the other two
        nums.sort()
        l, res = len(nums), 0        
        for i in xrange(l-1,1,-1):
            j, k = 0, i - 1                  
            while j < k:               
                if (nums[i] < nums[j] + nums[k]):                      
                    res += k - j
                    k -= 1                                    
                else:
                    j += 1
        return(res)