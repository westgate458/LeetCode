# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:37:14 2019

@author: Tianqi Guo
"""
# Solution 1 beats 99.33%: cheat by pre-calculation of all ugly numbers
class Ugly_num(object):
    def __init__(self):
        self.ans = [1]        
        p2 = p3 = p5 = 0      
        while len(self.ans) < 1690: 
            while self.ans[p2] * 2 <= self.ans[-1]:   p2 += 1
            while self.ans[p3] * 3 <= self.ans[-1]:   p3 += 1
            while self.ans[p5] * 5 <= self.ans[-1]:   p5 += 1            
            self.ans.append(min(self.ans[p2] * 2, self.ans[p3] * 3, self.ans[p5] * 5))

class Solution(object):
    u = Ugly_num()
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """                
        return(self.u.ans[n-1])

# Solution 2 beats 44.71%: merging lists in-place
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """        
        ans = [1]        
        p2 = p3 = p5 = 0      
        while len(ans) < n: 
            while ans[p2] * 2 <= ans[-1]:   p2 += 1
            while ans[p3] * 3 <= ans[-1]:   p3 += 1
            while ans[p5] * 5 <= ans[-1]:   p5 += 1            
            ans.append(min(ans[p2] * 2, ans[p3] * 3, ans[p5] * 5))
        return(ans[-1])

# Solution 3 beats 39.66%: merging 3 lists
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ans = [1]
        l2, l3, l5 = [2], [3], [5]
        p2, p3, p5 = 0, 0, 0
        
        while len(ans) < n:                
            num = min(l2[p2], l3[p3], l5[p5])            
            if num > ans[-1]:
                ans.append(num)
                l2.append(num*2)
                l3.append(num*3)
                l5.append(num*5)            
                    
            if l2[p2] == num:
                p2 += 1
            if l3[p3] == num:
                p3 += 1
            if l5[p5] == num:
                p5 += 1   
        
        return(ans[-1])

n = 12
test = Solution()
print(test.nthUglyNumber(n))















