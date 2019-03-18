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
        # if more than 12 digits, definitely illegal expression
        if len(s) > 12:
            # no way to decode as IP address
            return []
        
        # list storing all possible IP addresses
        self.ans = []

        # subfunction for trying out all combinations
        def DFS(s, n, IP):            
            # s: remaining string
            # n: remaining octets
            # IP: current decoded IP address
            
            # if has reached the last octet (group of number)
            if n == 0:
                # if all digits have been used in s
                if s == '':
                    # current decode is proper, store in the the answer list
                    self.ans.append(IP[1:])    
            
            # if more octets are needed
            # and remaining string is not empty
            elif s != '':
                
                # first continue DFS with current digit as one octet
                DFS(s[1:],n-1,IP+'.'+s[0])
                
                # length of remaining string
                l = len(s)
                # if more than one digit remaining, and current digit is not zero
                if l >= 2 and s[0] != '0':
                    # try DFS using next two digits as one octet
                    DFS(s[2:],n-1,IP+'.'+s[0:2])         
                    # if no fewer than 3 digits remaining, 
                    # and next 3 digits smaller than 255
                    if l>= 3 and (s[0] == '1' or (s[0] == '2' and (s[1] < '5' or (s[1] == '5' and s[2] <= '5')))): 
                        # continue DFS using next 3 digits as one octet
                        DFS(s[3:],n-1,IP+'.'+s[0:3])       
        
        # start DFS using all digits in the string, with four octets to go and empty IP address to fill
        DFS(s, 4, '')
        # return the answer list
        return self.ans

s = "172162541"  
test = Solution()
print test.restoreIpAddresses(s)
                
            
            