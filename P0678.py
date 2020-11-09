class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # scan string and record max and min numbers of possible open brackets until now
        left_min = left_max = 0        
        
        for c in s:
            if c == '(': 
                left_min += 1
            else: 
                left_min -= 1
                if left_min < 0: 
                    left_min = 0
                
            if c == ')': 
                left_max -= 1
                if left_max < 0: 
                    return False
            else: 
                left_max += 1
                
        return left_min==0