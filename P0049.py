# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 20:07:22 2018

@author: Tianqi Guo
"""



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """   
        ans = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if not (s_sorted in ans):
                ans[s_sorted] = [s]
            else:
                ans[s_sorted].append(s)

        return ans.values()
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = Solution()
print(test.groupAnagrams(strs))