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
        q = []
        for p in sorted(people, key=lambda p:(-p[0],p[1])):
            q.insert(p[1],p)
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