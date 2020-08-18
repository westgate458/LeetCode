class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
		# P0008 Next Permutation   
        s = list(str(n))         
        if s == sorted(s,reverse=True): return -1
        i = len(s) - 2
        while i > 0 and s[i] >= s[i+1]: i -=1 
        d = 10
        for j in xrange(i+1,len(s)):
            if s[j] > s[i] and ord(s[j]) - ord(s[i]) <= d:
                d, k = ord(s[j]) - ord(s[i]), j 
        s[i], s[k] = s[k], s[i]       
        res = int(''.join(s[:i+1] + s[i+1:][::-1]))        
        return -1 if res > 2147483647 else res