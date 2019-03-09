# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:26:29 2019

@author: Tianqi Guo
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        
        self.ans = []

        def DFS(s, n, IP):            
      
            if n == 0:
                if s == '':
                    self.ans.append(IP[1:])    
                    
            elif s != '':
                
                DFS(s[1:],n-1,IP+'.'+s[0])
                l = len(s)
                
                if l >= 2 and s[0] != '0':
                    DFS(s[2:],n-1,IP+'.'+s[0:2])                
                    if l>= 3 and (s[0] == '1' or (s[0] == '2' and (s[1] < '5' or (s[1] == '5' and s[2] <= '5')))): 
                        DFS(s[3:],n-1,IP+'.'+s[0:3])       
                        
        DFS(s, 4, '')
        return self.ans

s = "172162541"  
test = Solution()
print test.restoreIpAddresses(s)
                
            
            