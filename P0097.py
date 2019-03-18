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
        # length of each string
        l1, l2, l3 = len(s1), len(s2), len(s3)
        
        # if sum of lengths for s1 and s2 not equal to length of s3
        # or s1 + s2 do not contain same characters as s3
        if (l1 + l2 != l3) or (''.join(sorted(s3)) != ''.join(sorted(s1+s2))):
            # s3 is not interleaving from s1 and s2
            return False
        
        # the state function, if current substring is an interleaving string
        # 1D since we update each row only
        f = [True] * (l2+1)        
        
        # boundary conditions, when no parts from s2 are used
        for j in range(l2):
            # current substring is interleaving only if previous substring is
            # and current character match
            f[j+1] = f[j] and s2[j] == s3[j]            
        
        # update each row by considering more characters from s1
        for i in range(1,l1+1):
            # f[0] corresponds to no character from s2 are used
            # f[0] is true only if f[0] for previous substring from s1 is true
            # and current character in s1 matches s3
            f[0] = f[0] and s1[i-1] == s3[i-1]
            
            # gradually take more characters from s2 into interleaving
            for j in range(1,l2+1):
                # f[i][j] is true only if 
                # 1) f[i-1][j] is true, i.e. previous substring in s1 and s2 forms previous s3,
                #    and current character in s1 matches s3, or
                # 2) f[i][j-1] is true, i.e. previous substring in s1 and s2 forms previous s3,
                #    and current character in s2 matches s3
                f[j] = (f[j] and s1[i-1] == s3[i+j-1]) or (f[j-1] and s2[j-1] == s3[i+j-1])
        
        # the last state corresponds to if s3 is interleaving by whole s1 and s2
        return f[-1]
            
        
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
test = Solution()
print test.isInterleave(s1, s2, s3)