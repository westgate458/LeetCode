class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """      
		# only several cases to check one by one
        if not (set(b).issubset(set(a))): return -1
        c = len(b)//len(a)
        s = a * c
        if b in s: return c
        elif b in (s+a): return c+1
        elif b in (s+a+a): return c+2
        return -1