class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
		# LCM and LCD
        def GCD(a, b):
            while b != 0:                
                a, b = b, a%b                
            return a
        
        numerators, denominators, d, n, res = [], [], 1, '', 0
     
        for i, c in enumerate(expression+'+'):
            if c in '+-':
                if n:
                    denominators.append(int(n))
                    d *= denominators[-1]
                n = c
            elif c == '/':
                numerators.append(int(n))
                n = ''
            else:
                n += c        
        
        for numerator, denominator in zip(numerators,denominators):
            res += numerator * d/denominator
        
        gcd = GCD(res,d)
        return(str(res/gcd)+'/'+str(d/gcd))
        
        
        