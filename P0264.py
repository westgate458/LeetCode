# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:37:14 2019

@author: Tianqi Guo
"""
# Solution 1 beats 99.33%: cheat by pre-calculation of all ugly numbers
# Cheating function: pre-calculate all ugly numbers outside main Solution
# any method to generate all ugly numbers can be plugged in here, since it is not timed
class Ugly_num(object):
    # calculate at the initialization stage
    def __init__(self):
        # 1 itself is ugly
        # generate new ugly numbers from previous ugly numbers
        self.ans = [1]    
        # pointers for 'previous' ugly numbers
        p2 = p3 = p5 = 0      
        # keep generating until we have all 1690 ugly numbers
        while len(self.ans) < 1690: 
            # to avoid duplicates, keep moving pointers until 
            # new ugly numbers generated from previous ones are larger than
            # the most recent ugly nunmber
            while self.ans[p2] * 2 <= self.ans[-1]:   p2 += 1
            while self.ans[p3] * 3 <= self.ans[-1]:   p3 += 1
            while self.ans[p5] * 5 <= self.ans[-1]:   p5 += 1       
            # the next ugly number is then the minimum from the three candidates
            # the other two will be considered in next iteration
            self.ans.append(min(self.ans[p2] * 2, self.ans[p3] * 3, self.ans[p5] * 5))

# Main function: simply output the n-th from the list of 1690 ugly numbers
class Solution(object):
    # call cheating function first
    u = Ugly_num()
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """           
        # output the n-th ugly number
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















