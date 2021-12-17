class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        n_left_remains = n_right_allowed = 0         
        for c in s:
            if c == '(': n_left_remains += 1
            else:
                n_left_remains -= 1
                if n_left_remains < 0: n_left_remains = 0                
            if c == ')': n_right_allowed -= 1
            else: n_right_allowed += 1                
            if n_right_allowed < 0: return False            
        return n_left_remains==0
