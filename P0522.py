from collections import Counter
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
		# sort then check if is subsequence
        def check_sub(y,x):            
            it = iter(y)
            return all(c in it for c in x)
        counts = Counter(strs)           
        ss = sorted(counts.keys(),key=len,reverse=True)
        for i, s in enumerate(ss):
            if counts[s] != 1: continue  
            if not any(check_sub(v, s) for v in ss[:i]): return(len(s))            
        return(-1)