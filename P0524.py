class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """         
		# sort then check if is subsequence		
        for w in sorted(d,key=lambda x:(-len(x),x)):   
            it = iter(s)
            if all(c in it for c in w): return w
        return ''