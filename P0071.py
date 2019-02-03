# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 20:24:56 2019

@author: Tianqi Guo
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        folders = path.split('/')
        stack = []

        for folder in folders:    
            if (folder == '') or (folder == '.'):
                continue
            elif folder == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)

        if stack:
            ans = ''.join('/' + folder for folder in stack)
        else:
            ans = '/'   
            
        return ans

path = "/a//b////c/d//././/.."
test = Solution()
print test.simplifyPath(path)