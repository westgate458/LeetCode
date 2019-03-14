# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:51:56 2019

@author: Tianqi Guo
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        l1, l2, l3 = len(s1), len(s2), len(s3)
        
        if (l1 + l2 != l3) or (''.join(sorted(s3)) != ''.join(sorted(s1+s2))):
            return False
        
        f = [True] * (l2+1)        

        for j in range(l2):
            f[j+1] = f[j] and s2[j] == s3[j]
            if not f[j+1]:
                break
              
        for i in range(1,l1+1):
            f[0] = f[0] and s1[i-1] == s3[i-1]
            for j in range(1,l2+1): 
                f[j] = (f[j] and s1[i-1] == s3[i+j-1]) or (f[j-1] and s2[j-1] == s3[i+j-1])
                
        return f[-1]
            
        
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
test = Solution()
print test.isInterleave(s1, s2, s3)