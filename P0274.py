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
        # initialize h-index with 0
        h = 0
        # sort citations in descending order
        # then start from the highest cited work
        # try to increase h-index by 1 each time
        for citation in sorted(citations, reverse = True):             
            # try to increase h-index by 1
            h += 1            
            # if current citation is smaller than h-to-be
            # it means for the previous (h-1) citations, they are all larger than (h-1)
            # while the remaining (N-(h-1)) citations, they are all smaller than (h-1)
            # that is the definition of h-index
            if citation < h:                
                # so the previous h value is the h-index for this set of citations
                return h-1     
        # deal with trivial case
        return(h)        

citations = [100]
citations = [3,0,6,1,5]
test = Solution()
print(test.hIndex(citations))