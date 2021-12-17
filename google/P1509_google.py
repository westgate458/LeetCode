class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4: return(0)
        a1 = a2 = a3 = a4 = 10**9
        b1 = b2 = b3 = b4 = -10**9
        
        for num in nums:
            if num < a4:
                if num < a3:
                    if num < a2:
                        if num < a1: a1, a2, a3, a4 = num, a1, a2, a3
                        else: a2, a3, a4 = num, a2, a3
                    else: a3, a4 = num, a3
                else: a4 = num
            if num > b4:
                if num > b3:
                    if num > b2:
                        if num > b1: b1, b2, b3, b4 = num, b1, b2, b3
                        else: b2, b3, b4 = num, b2, b3
                    else: b3, b4 = num, b3
                else: b4 = num                            
                
        return(min([b1-a4,b2-a3,b3-a2,b4-a1]))