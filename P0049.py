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
        
        # answer dictionary
        # sorted string as key, original strings as values
        ans = {}
        
        # deal with each string in the list
        for s in strs:
            # sort the string as dictionary key
            s_sorted = ''.join(sorted(s))
            # check if the key doesn't exist yet
            if not (s_sorted in ans):
                # create a new key and store the original string
                ans[s_sorted] = [s]
            # if the key already existes
            else:
                # update values by adding the new string
                ans[s_sorted].append(s)
        
        # return the values of the dictionary
        return ans.values()
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = Solution()
print(test.groupAnagrams(strs))