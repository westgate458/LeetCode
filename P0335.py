# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:45:28 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        # deal with trivial case
        if len(x) < 4:
            return False        
        # previous four lengths
        l1, l2, l3, l4 = 0, x[0], x[1], x[2] 
        # check if sequence is an increasing spiral
        increasing = x[2] > x[0]       
        # check each length afterwards
        for i in x[3:]:         
            # if we have an increasing spiral
            if increasing:
                # and current length is longer than its parallel previous one
                if i > l2:
                    # no crossing, we udpate lengths and move on
                    l1, l2, l3, l4 = l2, l3, l4, i
                # or current length is no longer than its parallel previous one
                else:
                    # from now on we should look for a decreasing spiral within the previous increasing one
                    increasing = False
                    # now there are two scenarios
                    # 1) current length is within the opening of previous spiral
                    if i + l1 < l3:
                        # no crossing at current step, we udpate lengths and move on
                        l1, l2, l3, l4 = l2, l3, l4, i
                    # 2) current length has exceeded the opening from previous spiral
                    else:
                        # for next step, it has a narrower window for no-crossing
                        # we update l2 with more strict condition
                        l1, l2, l3, l4 = l2, l4-l2, l4, i
            # if we have a decreasing spiral
            else:
                # current length can not exceed its parallel previous one
                if i >= l2:
                    # crossing found
                    return True
                # if no crossing, we udpate lengths and move on
                else:
                    l1, l2, l3, l4 = l2, l3, l4, i
        # if all lengths are checked and no crossing, we good
        return False
            