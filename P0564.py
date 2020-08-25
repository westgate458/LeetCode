class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
		# choose from fixed numbers of candidates
        l, nn = len(n), int(n)
        s, m = set([10**l - 1, 10**l + 1, 10**(l-1) - 1, 10**(l-1) + 1]), l%2        
        half = int(n[:l//2+m])
        for left in [half-1, half, half+1]:
            ss = str(left)
            s.add(int(ss + (ss[:-1] if m else ss)[::-1]))        
        if nn in s: s.remove(nn)        
        return str(sorted(s, key=lambda x:(abs(x-nn),x))[0])