class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check(s,l):
            d = set()
            for i in range(len(s)-l+1):                
                if s[i:i+l] in d: return s[i:i+l]
                else: d.add(s[i:i+l])            
            return ''        
        res, lo, hi = '', 1, len(s)  
        while lo <= hi:
            m = (lo+hi)//2
            ss = check(s,m)            
            if ss:
                lo = m + 1
                res = ss
            else:
                hi = m - 1            
        return(res)