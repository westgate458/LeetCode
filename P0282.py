# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:14:04 2019

@author: Tianqi Guo
"""

class Solution(object):    
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # Solution 1 beats 99.30%: keep previous sum and decide if to update
        if not num:
            return []
        ans = []
        nums = [int(x) for x in num]
        def helper(p, combo, prod, preSum, curNum):
            if p == len(num) - 1:
                if preSum + prod + nums[p] == target:
                    ans.append(combo + '+' + num[p])
                if preSum + prod - nums[p] == target:
                    ans.append(combo + '-' + num[p])
                if preSum + prod * nums[p] == target:
                    ans.append(combo + '*' + num[p])
                if curNum and preSum + prod * 10 + prod//curNum*nums[p] == target:
                    ans.append(combo + num[p])
            else:
                helper(p+1, combo+'+'+num[p], nums[p], preSum + prod, nums[p])
                helper(p+1, combo+'-'+num[p], -nums[p], preSum + prod, nums[p])
                helper(p+1, combo+'*'+num[p], prod * nums[p], preSum, nums[p])
                if curNum:
                    helper(p+1, combo+num[p], prod * 10 + prod//curNum*nums[p], preSum, 10*curNum+nums[p])
        helper(1, num[0], nums[0], 0, nums[0])
        return ans
                    
            
        #Solution 2 beats 66.53%: reverse previous operation
#        self.combos = set([])
#        self.target = target
#        def helper(num, combo, pre_num, pre_op, result):     
#            if num == '' and self.target == result:                
#                self.combos.add(combo)
#                return
#            else:
#                for i in range(len(num)):
#                    s = num[0:i+1]
#                    n = int(s)                   
#                    helper(num[i+1:], combo + '+' + s, n, '+', result + n)
#                    helper(num[i+1:], combo + '-' + s, n, '-', result - n)
#                    if pre_op == '+':
#                        helper(num[i+1:], combo + '*' + s, pre_num * n, '+', result - pre_num + pre_num * n)
#                    elif pre_op == '-':
#                        helper(num[i+1:], combo + '*' + s, pre_num * n, '-', result + pre_num - pre_num * n)
#                    if n == 0:
#                        break                    
#        for i in range(len(num)):
#            s = num[0:i+1]
#            n = int(s)                   
#            helper(num[i+1:], s, n, '+', n)
#            if n == 0:
#                break 
#        return(list(self.combos))


num = "105"
target = 5
num = "00"
target = 0
num = "345623749"
target = 9191
num = "1000000009"
target = 9
num = "232"
target = 8
num = '123'
target = 6

test = Solution()
print(test.addOperators(num, target))