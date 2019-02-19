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
        
        # split the path by '/'
        folders = path.split('/')
        # stack that stores the simplified path
        stack = []
        
        # deal with each folder along the path
        for folder in folders:  
            # 'empty folder name' or 'stay in current folder' is found
            if (folder == '') or (folder == '.'):
                # do nothing, move on to next folder
                continue
            # 'return to parent folder' is found
            elif folder == '..':
                # if there is a previous folder in the stack
                if stack:
                    # remove top folder to return to parent folder
                    stack.pop()
            # regular folder name is found
            else:
                # put current folder into stack
                stack.append(folder)
        
        # if stack is not empty
        if stack:
            # join the folders in stack with '/'
            ans = ''.join('/' + folder for folder in stack)
        # if stack is empty
        else:
            # default root folder
            ans = '/'   
        
        # return simplified path
        return ans

path = "/a//b////c/d//././/.."
test = Solution()
print test.simplifyPath(path)