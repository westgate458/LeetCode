class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """     
		# check if two hash tables are equal
        l1, l2 = len(s1), len(s2)        
        if (l1 > l2) or (not set(s1).issubset(set(s2))): return False        
        d1, d2 = [0]*26, [0]*26
        n1 = map(lambda c:ord(c)-ord('a'),list(s1))
        n2 = map(lambda c:ord(c)-ord('a'),list(s2))
        for i in range(l1): 
            d1[n1[i]] += 1
            d2[n2[i]] += 1           
        if d1 == d2: return True
        for i in range(l1,l2):           
            d2[n2[i-l1]] -= 1
            d2[n2[i]] += 1
            if d1 == d2: return True    
        return False