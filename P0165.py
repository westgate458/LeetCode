# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:07:24 2019

@author: Tianqi Guo
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        # Solution 1: using map function        
        # split two strings at '.'s and convert to list of numbers
        n1, n2 = map(int, version1.split('.')), map(int, version2.split('.'))
        # lengths of two number lists
        l1, l2 = len(n1), len(n2)
        # pad two lists with 0's to have equal lengths
        if l1 > l2:
            n2 = n2 + [0]*(l1-l2)
        elif l1 < l2:
            n1 = n1 + [0]*(l2-l1)            
        # check each sub version number between the two
        for x, y in zip(n1,n2):            
            # for current subversion number
            # the larger number corresponds to the newer version
            if x > y:
                # version1 newer
                return 1
            elif x < y:
                # version2 newer
                return -1 
        # two versions are identical
        return 0
        
#        # Solution 2: straight-forward        
#        s1, s2 = version1.split('.'), version2.split('.')
#        l1, l2 = len(s1), len(s2)
#        p1 = p2 = 0        
#        while p1 < l1 or p2 < l2:            
#            n1 = int(s1[p1]) if p1 < l1 else 0
#            n2 = int(s2[p2]) if p2 < l2 else 0 
#            if n1 == n2:
#                p1 += 1
#                p2 += 1
#            elif n1 > n2:
#                return 1
#            else:
#                return -1        
#        return 0


version1 = "0.1"
version2 = "1.1"

version1 = "1.0.1"
version2 = "1"

version1 = "1.0"
version2 = "1.0.0"

version1 = "1"
version2 = "0"

version1 = "7.5.2.4"
version2 = "7.5.3"

test = Solution()
print test.compareVersion(version1, version2)
