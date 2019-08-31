# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:22:39 2019

@author: Tianqi Guo
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        for citation in sorted(citations, reverse = True): 
            h += 1            
            if citation < h:                
                return h-1     
        return(h)
        

citations = [100]
citations = [3,0,6,1,5]
test = Solution()
print(test.hIndex(citations))