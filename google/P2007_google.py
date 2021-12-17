class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        res = []        
        changed_set = Counter(changed)
        for m in sorted(changed):            
            if (changed_set[m]==0): continue
            changed_set[m] -= 1
            if (changed_set[2*m]==0): return []
            res.append(m)                
            changed_set[2*m] -= 1 
        return res