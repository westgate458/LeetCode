class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = len(s)
        pos = [-1] * 26
        
        left = [-1]*l 
        for i in range(l):
            if pos[ord(s[i])-ord('A')] != -1:
                left[i] = pos[ord(s[i])-ord('A')]
            pos[ord(s[i])-ord('A')] = i
        
        pos = [-1] * 26
        right = [-1]*l
        for i in range(l-1,-1,-1):
            if pos[ord(s[i])-ord('A')] != -1:
                right[i] = pos[ord(s[i])-ord('A')]
            pos[ord(s[i])-ord('A')] = i
        
        res = 0
        for i in range(l):            
            ll = 0 if left[i]==-1 else left[i]+1            
            rr = l-1 if right[i]==-1 else right[i]-1           
            
            res += (i-ll+1)*(rr-i+1)
        return res