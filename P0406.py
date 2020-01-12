# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:52:05 2020

@author: Tianqi Guo
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Solution 1 beats 71.12%: start from tallest person
        # q is the reconstructed queue
        q = []
        # first we sort p, first based on height in reversed order
        # then based on the the number of people in front of this person who have a height greater than or equal to
        # in such a way we insert tall people first in to the queue
        # then for shorter people since all people taller than them have already been inserted
        # their position is simply the number in p[1]
        for p in sorted(people, key=lambda p:(-p[0],p[1])):
            q.insert(p[1],p)
        # return the reconstructed queue
        return q
    
        # Solution 1 beats 22.09%: start from shortest person
        people.sort()
        inds = range(len(people))
        queue = [(0,0) for _ in inds]
        ind_delete = []
        pre_h = -1
        while people:
            h,k = people.pop(0)
            if h != pre_h:
                for ind in ind_delete:
                    inds.remove(ind)
                ind_delete = []
            queue[inds[k]] = (h, k)
            ind_delete.append(inds[k])
            pre_h = h
        return(queue)