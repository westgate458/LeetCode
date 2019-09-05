# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:36:15 2019

@author: Tianqi Guo
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """     
        # total citations
        l = len(citations)   
        # head and tail pointers for binary search
        h, t = 0, l - 1        
        # continue searching till two pointers meet  
        # thats when head is the work that is associated with h-index
        # i.e. all papers after current head have at least h citations each, 
        # and all papers before current head have no more than h citations each
        while h <= t:            
            # the middle point
            m = (h + t)/2
            # if current citation number is larger than the distance from the end
            # i.e. current citations larger than number of works after current
            if citations[m] >= l - m:
                # then the work associated with the h-index is before current middle
                t = m - 1
            # if the current citations smaller than number of works after current
            else:
                # then the work associated with the h-index is after current middle
                h = m + 1
        # return the number of papers after current head, i.e. the h-index
        return l - h

citations = [0,1,3,5,6]
citations = [1,2]
citations = [0, 1]
citations = [11,15]

citations = [100]

test = Solution()
print(test.hIndex(citations))