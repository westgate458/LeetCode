# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:36:40 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # number of occurances of each character in the sliding window
        counts = defaultdict(int)
        # l: position of left pointer
        # res: largest window\longest string found
        # mc: max count of occurances within the window
        l, res, mc = 0, 0, 0
        # move the right pointer one character each time
        for r in xrange(len(s)):
            # update the count of the new character
            counts[s[r]] += 1
            # see if it appears more than previous max count
            mc = max(mc, counts[s[r]])
            # the number of replacement needed for this window of length res
            # is res - mc, if res - mc < k, it is possible to have only one repeating character
            if mc + k > res:
                # we update the length of the window\string
                res += 1
            # if not, we move the window towards right in next iteration
            # without extending its length
            else:
                # remove the left most character from the window
                counts[s[l]] -= 1
                # update the left pointer
                l += 1                
        # return the max length found
        return res