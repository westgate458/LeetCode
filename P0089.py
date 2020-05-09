# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:09:16 2019

@author: Tianqi Guo
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """    
#        # less efficient dfs version
#        def dfs(s, d, code):                    
#            if d == 1:       
#                return code              
#            num = int(s,2)
#            flag[num] = 1            
#            for c in range(len(s)):
#                if s[c] == '0':
#                    ss = s[:c] + '1' + s[c+1:]
#                else:
#                    ss = s[:c] + '0' + s[c+1:]
#                new_num = int(ss,2)
#                if flag[new_num] == 0:
#                    ans = dfs(ss,d-1,code + [new_num])
#                    if ans:
#                        return ans                    
#            flag[num] = 0
#            return None        
#        flag = [0] * 2**n
#        s_0 = '0' * n
#        return dfs(s_0, 2**n, [0])
        
        # build gray code for (n) from (n-1) by
        # 1) reversing the entries for the gray codes of (n-1)
        # 2) prefixing the entries in the the gray codes of (n-1) with a binary 0,
        #    for decimal (0 + entry)_2 is just keeping the entries as they are
        # 3) prefixing the entries in the reversed list with a binary 1
        #    for decimal (1 + entry)_2 = (2^i + entry)_10 for entry in reversed order
        # 4) concatenating the original list with the reversed list.
        
        # start from gray codes for n = 0
        ans = [0]
        # construct the gray codes one by one
        for i in range(n):
            # gray codes for n is
            # [entries from gray codes for (n-1)] + [2^i + entries from reversed gray codes for (n-1)]
            ans = ans + [x + 2**i for x in ans[::-1]]
        
        # return gray codes for current n
        return ans
    
n = 4
test = Solution()
print test.grayCode(n)
