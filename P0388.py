# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:55:17 2019

@author: Tianqi Guo
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # ans - longest length
        # s - stack for previous folders
        # l - stack for previous levels
        ans, s, l = 0, [], [-1]      
        # split the input string by \n, and check each folder
        for path in input.split("\n"):
            # its level is simply how many \t it has
            level = path.count('\t')
            # keep popping previous folder 
            # if it is not the parent folder of current one
            while level <= l[-1]:
                l.pop()
                s.pop()
            # push current folder and level to the stacks
            s.append(path.lstrip('\t'))
            l.append(level)
            # compare with answer if current folder is a file (it has '.' in name)
            if '.' in path:                
                # update answer length
                ans = max(ans, len('/'.join(s)))
        # return answer length
        return(ans)