class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res, last = '', 0                
        for _, i in sorted(zip(indices, range(len(indices)))):
            if s[indices[i]:indices[i]+len(sources[i])] == sources[i]:
                res += s[last:indices[i]] + targets[i]
                last = indices[i] + len(sources[i])      
            else:
                res += s[last:indices[i]]  
                last = indices[i]                 
        return res+s[last:]