class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """  
        def not_sub(s1,s2):
            i = 0
            for c in s1:
                j = s2.find(c,i)
                if j == -1: return True
                else: i = j+1
            return False            
        c = Counter(strs)
        ss = []
        for s in sorted(strs,key=len,reverse=True):
            if c[s] == 1 and all([not_sub(s,t) for t in ss]): return len(s)   
            ss.append(s)
        return -1