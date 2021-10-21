class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        c = Counter(arr)
        res = len(c)
        for i,j in sorted(c.items(),key=lambda x:x[1]):
            if k >= j:
                k -= j
                res -= 1
            else:
                break
        return res
                
        
        