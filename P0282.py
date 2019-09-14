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
        # deal with trivial case
        if not num:
            return []
        # ans for all combos
        ans = []
        # convert all str to nums
        nums = [int(x) for x in num]
        # DFS function to solve subproblems
        def helper(p, combo, prod, preSum, curNum):
            # p: pointer to current digit
            # combo: current combination of nums and ops
            # preSum: previous sum before prod begins
            # prod: (with sign) running product from previous digits             
            # curNum: (always non-negative) current number that current digit can be appended to 
            # prod//curNum gives the +/- before prod begins
            
            # if we have reached the last digit
            if p == len(num) - 1:
                # check four possible outcomes, see if the target is achieved
                # 1) current digit is treated as one number alone, op is +
                if preSum + prod + nums[p] == target:
                    ans.append(combo + '+' + num[p])
                # 2) current digit is treated as one number alone, op is -
                if preSum + prod - nums[p] == target:
                    ans.append(combo + '-' + num[p])
                # 3) current digit is treated as one number alone, op is *
                if preSum + prod * nums[p] == target:
                    ans.append(combo + '*' + num[p])
                # 4) current digit is appended to previous number
                if curNum and preSum + prod * 10 + prod//curNum*nums[p] == target:
                    ans.append(combo + num[p])
            # if we have not reached the last digit yet
            else:
                # continue DFS in the following 4 directions
                # 1-3) take current digit as one number alone
                #      try ops +/-/*, update prod, preSum  
                #      and take current digit as current number
                helper(p+1, combo+'+'+num[p], nums[p], preSum + prod, nums[p])
                helper(p+1, combo+'-'+num[p], -nums[p], preSum + prod, nums[p])
                helper(p+1, combo+'*'+num[p], prod * nums[p], preSum, nums[p])
                # 4) append current digit to previous number
                if curNum:
                    helper(p+1, combo+num[p], prod * 10 + prod//curNum*nums[p], preSum, 10*curNum+nums[p])
        # start DFS from the 1st digit
        helper(1, num[0], nums[0], 0, nums[0])
        # return all found combinations
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