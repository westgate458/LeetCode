class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
		# deal with coefficients and constants separately
        n, coef, num, is_left = '', 0, 0, 1        
        for c in equation+'+':      
            if (not n) or (c in '0123456789x'):
                n += c
            else:            
                if n[-1] == 'x':                    
                    if n in ['x','+x']:
                        coef += is_left
                    elif n == '-x':
                        coef -= is_left
                    else:                        
                        coef += is_left * int(n[:-1])                      
                else:   
                    num -= is_left*int(n)                    
                if c == '=':
                    is_left, n = -1, ''                    
                else:
                    n = c   
        if coef == 0:
            return 'Infinite solutions' if num == 0 else 'No solution'            
        else:
            return 'x=%d'%(num/coef)