# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:09:16 2019

@author: Administrator
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """      
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
        
        ans = [0]
        for i in range(n):
            ans = ans + [x + 2**i for x in ans[::-1]]
            
        return ans
    
n = 4
test = Solution()
print test.grayCode(n)
